import json
import math
import os
import threading
import argparse
from threading import Thread

import requests

MP3_FILENAME_EXTENSION = '.mp3'
DATA_FILE = 'ultimate.json'


def download_mp3(word, urls, dir_path):
    for url in urls:
        filename = os.path.join(dir_path, word + MP3_FILENAME_EXTENSION)
        try:
            content = requests.get(url).content
        except requests.RequestException:
            continue
        if not is_mp3(content):
            continue
        with open(filename, 'wb') as file:
            file.write(content)
            return
    raise Exception('No valid link was found')


# split a dictionary into a list of dictionaries
def split_dict_evenly(m_dict, segment_count):
    if segment_count == 1:
        return [m_dict]

    segment_length = math.ceil(len(m_dict) / segment_count)
    keys = list(m_dict.keys())
    key_groups = [keys[segment_length * i: segment_length * (i + 1)] for i in range(segment_count)]
    return [{key: m_dict[key] for key in group} for group in key_groups]

def is_mp3(binary_data):
    return any(binary_data.startswith(bytearray.fromhex(header)) for header in ['fffb', '494433'])

def sort_urls_by_preferences(urls, preferences):
    if not preferences:
        return urls

    def index_of_url(url):
        for (i, preference) in enumerate(preferences):
            if preference in url:
                return i
        return len(preferences)

    return sorted(urls, key=lambda url: index_of_url(url))


# a single downloader thread
class DownloadWorker(Thread):
    # 'pairs' is a dictionary
    def __init__(self, pk, pairs, dir_path, statistics, silent, preferences):
        Thread.__init__(self)
        self.pk = pk
        self.pairs = pairs
        self.dir_path = dir_path
        self.statistics = statistics
        self.silent = silent
        self.preferences = preferences

    def run(self):
        for word, urls in self.pairs.items():
            # if os.path.exists(os.path.join(self.dir_path, word + MP3_FILENAME_EXTENSION)):
            #     self.statistics.decrease_total()
            #     continue
            urls = sort_urls_by_preferences(urls, self.preferences)
            try:
                download_mp3(word, urls, self.dir_path)
                if not self.silent:
                    print('Success on %s' % word)
            except Exception as exc:
                if not self.silent:
                    print('Failed on %s: %s' % (word, str(exc)))
            current = self.statistics.increase_current()
            if not self.silent:
                print('(' + str(current) + '/' + str(self.statistics.total) + ') ')


# provide a mutex on a shared integer representing current progress
class Statistics:
    # pass in the total number in the constructor
    def __init__(self, total):
        self.total = total
        self.current = 0
        self.total_lock = threading.Lock()
        self.current_lock = threading.Lock()

    # an atom operation to increase the current progress
    def increase_current(self):
        self.current_lock.acquire()
        self.current += 1
        value = self.current
        self.current_lock.release()
        return value

    def decrease_total(self):
        self.total_lock.acquire()
        self.total -= 1
        value = self.total
        self.total_lock.release()
        return value

def word_to_default_representation(word):
    return word.strip().lower()


def main(total_threads, dir_path, words, silent, preferences):
    # create directory
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # load data into dictionary
    with open(DATA_FILE, 'r') as file:
        data = json.loads(file.read())

    if words:
        data = {
            word: urls
            for (word, urls) in data.items()
            if word_to_default_representation(word) in words
        }
        if not silent:
            for word in words:
                if word not in data.keys():
                    print('Could not find %s in dictionary' % word)


    # split dictionary into a list of dictionaries, each for a thread
    data_segments = split_dict_evenly(data, total_threads)

    # initialize shared object statistics
    statistics = Statistics(len(data))

    # start downloader threads
    for i in range(total_threads):
        worker = DownloadWorker(i + 1, data_segments[i], dir_path, statistics, silent, preferences)
        worker.start()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--threads', default=30, help='Number of threads for downloading.'
                                                            ' By default 30.')
    parser.add_argument('-d', '--directory', default='download', help='Directory to put downloaded words into.'
                                                                       ' By default "download/".')
    parser.add_argument('-w', '--words', default=None,
                        help='Words to download, separated with commas.'
                             ' Example "apple, banana, clown".'
                             ' By default downloads all the words.')  # None stands for all the words
    parser.add_argument('-s', '--silent', default=False, action='store_true',
                        help='Keep silent.')
    parser.add_argument('-p', '--prefer', default=None,
                        help='Preferred website to download links from.'
                             ' Every argument should be a substring of this website name.'
                             ' Arguments should be separated with commas.'
                             ' Example of usage "-p amazonaws" which stands for oxford dictionaries.')
    return parser.parse_args()


def parse_arguments_list(arguments_list):
    return [word_to_default_representation(word) for word in arguments_list.split(',')] if arguments_list else None

if __name__ == '__main__':
    arguments = parse_args()
    main(
        arguments.threads,
        arguments.directory,
        parse_arguments_list(arguments.words),
        arguments.silent,
        parse_arguments_list(arguments.prefer),
    )
