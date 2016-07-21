# English Words Pronunciation MP3 Audio Download

## Introduction

This is a simple Python script to download the MP3 audio for 35,167 unique English words. They will take only 395.7 MB space on your disk.

If the word you are looking for is not in the list, you should probably try some other sources. Ask me for help if you wanna make a crawler for the source you found but you don't know how.

Also please let me know if the MP3 URLs don't work anymore. The owners may change the URLs at any time, but it's OK, coz we can always make a new crawler to find all the audio files again.

## Getting Started

* Download & install [Python 3](https://www.python.org/downloads/)
* Install dependencies

```bash
$ pip install -r requirements.txt
```

## Download All MP3

Just do it.

```bash
$ python3 download_all_mp3.py
```

This command will start a downloader with 30 threads by default.

To specify how many threads you want to use in the downloader, just pass in a positive integer as parameter:

```bash
$ python3 download_all_mp3.py 10
```

This will start a downloader with 10 concurrent threads. Honestly it's a good choice to use 30 threads. You don't really need to change this unless you have a clear reason to.

The downloaded mp3 audio files will be stored in the `download/` directory

## Use `data.json` in Other Applications

The [data.json](data.json) file contains the URLs to the pronunciation MP3 audio files for 35,167 unique English words.

I used my own crawler and it took quite a few hours to get all the data from the Web. Now you can use the data directly without writing your own crawler or wasting a few hours. The idea behind this is just like [rainbow tables](https://en.wikipedia.org/wiki/Rainbow_table). 

A segment of the `data.json` file looks like this:

```json
{
	"absurdity": "http://static.sfdict.com/staticrep/dictaudio/A00/A0042000.mp3",
	"absurdly": "https://s3.amazonaws.com/audio.vocabulary.com/1.0/us/A/1RFDX0TX7V5W2.mp3",
	"abundance": "http://static.sfdict.com/staticrep/dictaudio/A00/A0043200.mp3",
	"abundant": "http://static.sfdict.com/staticrep/dictaudio/A00/A0043300.mp3",
	"abundantly": "https://s3.amazonaws.com/audio.vocabulary.com/1.0/us/A/1IRP8L3BRTC7D.mp3",
	"abuse": "http://static.sfdict.com/staticrep/dictaudio/A00/A0043700.mp3",
	"abused": "https://s3.amazonaws.com/audio.vocabulary.com/1.0/us/A/1MF37OCP81MZF.mp3",
	"abuser": "https://s3.amazonaws.com/audio.vocabulary.com/1.0/us/A/4FIS2UDR6SLF.mp3",
	"abusive": "http://static.sfdict.com/staticrep/dictaudio/A00/A0044100.mp3",
	"abusively": "https://s3.amazonaws.com/audio.vocabulary.com/1.0/us/A/18VNGM45R1BB3.mp3",
	"abut": "http://static.sfdict.com/staticrep/dictaudio/A00/A0044200.mp3"
}
```

Apparently, each key is an English word and the value is the URL to the MP3 audio files.

The `data.json` file is only 2.9 MB so you can load it in the memory and let it serve as a lookup table. 

## Acknowledgements

The list of English words was downloaded from [Mieliestronk's](http://www.mieliestronk.com/wordlist.html). There are 56K+ words in the list but only 35K+ have pronunciation audio.

I'd like to deliever my special thanks to [dictionary.com](http://dictionary.com) for making their website so easily crawlable. The clear-text links are just in the html files.

[Vocabulary.com](http://www.vocabulary.com/) did play some simple trick to hide out the MP3 URLs on their website but it's not that hard to locate their bucket on Amazon S3. Nice try btw.
