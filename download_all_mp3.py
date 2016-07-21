import json
import math
import os
import sys
import threading
from threading import Thread

import requests

MP3_FILENAME_EXTENSION = '.mp3'
DIR_PATH = 'download/'
TOTAL_THREADS = 30
DATA_FILE = 'data.json'


def download_mp3(word, url, dir_path):
    filename = os.path.join(dir_path, word + MP3_FILENAME_EXTENSION)
    with open(filename, 'wb') as file:
        file.write(requests.get(url).content)


# split a dictionary into a list of dictionaries
def split_dict_evenly(m_dict, segment_count):
    if segment_count == 1:
        return [m_dict]

    segment_length = math.ceil(len(m_dict) / segment_count)
    keys = list(m_dict.keys())
    key_groups = [keys[segment_length * i: segment_length * (i + 1)] for i in range(segment_count)]
    return [{key: m_dict[key] for key in group} for group in key_groups]


# a single downloader thread
class DownloadWorker(Thread):
    # 'pairs' is a dictionary
    def __init__(self, pk, pairs, dir_path, statistics):
        Thread.__init__(self)
        self.pk = pk
        self.pairs = pairs
        self.dir_path = dir_path
        self.statistics = statistics

    def run(self):
        for word, url in self.pairs.items():
            # if os.path.exists(os.path.join(self.dir_path, word + MP3_FILENAME_EXTENSION)):
            #     self.statistics.decrease_total()
            #     continue
            current = self.statistics.increase_current()
            print('(' + str(current) + '/' + str(self.statistics.total) + ') ' + word)
            download_mp3(word, url, self.dir_path)


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


def main(total_threads):
    # create directory
    if not os.path.exists(DIR_PATH):
        os.makedirs(DIR_PATH)

    # load data into dictionary
    with open(DATA_FILE, 'r') as file:
        data = json.loads(file.read())

    # split dictionary into a list of dictionaries, each for a thread
    data_segments = split_dict_evenly(data, total_threads)

    # initialize shared object statistics
    statistics = Statistics(len(data))

    # start downloader threads
    for i in range(total_threads):
        worker = DownloadWorker(i + 1, data_segments[i], DIR_PATH, statistics)
        worker.start()


if __name__ == '__main__':
    argument = TOTAL_THREADS

    if len(sys.argv) == 2:
        argument = int(sys.argv[1])

    if argument > TOTAL_THREADS:
        argument = TOTAL_THREADS
    
    main(argument)
