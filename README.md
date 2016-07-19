# English Words Pronunciation MP3 Audio Download

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

This command will start a downloader with 50 threads by default.

To specify how many threads you want to use in the downloader, just pass in a positive integer as parameter:

```bash
$ python3 download_all_mp3.py 10
```

This will start a downloader with 10 concurrent threads.

The downloaded mp3 audio files will be stored in the `download/` directory

## Use `data.json` in Other Applications

The [data.json](data.json) file contains the URLs to the pronunciation mp3 audio files for over 24,000 English words.

A segment of the `data.json` file looks like this:

```json
{
	"aardvark": "http://static.sfdict.com/staticrep/dictaudio/A00/A0001900.mp3",
	"aardwolf": "http://static.sfdict.com/staticrep/dictaudio/A00/A0002000.mp3",
	"aback": "http://static.sfdict.com/staticrep/dictaudio/A00/A0003800.mp3",
	"abacus": "http://static.sfdict.com/staticrep/dictaudio/A00/A0004300.mp3",
	"abaft": "http://static.sfdict.com/staticrep/dictaudio/A00/A0004800.mp3",
	"abalone": "http://static.sfdict.com/staticrep/dictaudio/A00/A0005200.mp3",
	"abandoned": "http://static.sfdict.com/staticrep/dictaudio/A00/A0005700.mp3",
	"abase": "http://static.sfdict.com/staticrep/dictaudio/A00/A0006100.mp3",
	...
}
```

Apparently, each key is an English word and the value is the URL to the MP3 audio files.

The `data.json` file is only 1.8MB so you can load it in your memory and let it serve as a lookup table. This should have covered most unique words out there in English. If the word you are looking for is not in the list, you should probably look for some other sources. Ask me for help if you wanna make a crawler and you don't know how.

## Acknowledgements

The word list was downloaded from [Mieliestronk's](http://www.mieliestronk.com/wordlist.html). There are 56K+ words in the list but only 24K+ are recognized as unique words.

Finally thanks to [vocabulary.com](http://vocabulary.com) for making their website so easily crawlable. Google no longer provides such feature though. 
