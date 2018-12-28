# English Words Pronunciation MP3 Audio Download

## Introduction

This is a simple Python script to download the MP3 pronunciation audio for 119,377 unique English words/terms. They will take around 2 GB on your disk in total.

The MP3 sources were obtained from the following 7 online dictionaries:

* [Cambridge Dictionary](dictionary.cambridge.org/us/)
* [Oxford Dictionaries](https://www.oxforddictionaries.com/us)
* [Dictionary.com](http://www.dictionary.com/)
* [Vocabulary.com](https://www.vocabulary.com/)
* [YourDictionary](http://www.yourdictionary.com/)
* [The Free Dictionary](http://www.thefreedictionary.com/)
* [OneLook Dictionary Search](http://www.onelook.com/)

This project should have covered everything you might ever think of, from "[.22 caliber](http://s3.amazonaws.com/audio.vocabulary.com/1.0/us/0/RDDDYYYO4SJ7.mp3)" to "[zinc cadmium sulfide](http://s3.amazonaws.com/audio.vocabulary.com/1.0/us/Z/NJ4TGQ8X0UG6.mp3)"; from "[1000000000000](http://s3.amazonaws.com/audio.vocabulary.com/1.0/us/0/KZRW2TGIAGCV.mp3)" to "[level dependent functional magnetic resonance imaging](http://s3.amazonaws.com/audio.vocabulary.com/1.0/us/B/HY3Z3VF99Y86.mp3)" (YES, we have the pronunciation for this long term). If the word/term you are looking for is not in the list, it's most likely because the it didn't appear in any of the online dictionaries.

I currently don't have the intention to share the source code of my crawler framework that found these MP3 URLs. However, if there are more sites you wanna crawl but you don't know how to, ask me for help and I'll happily make a crawler for you.

## Getting Started

* Download & install [Python 3](https://www.python.org/downloads/)
* Install dependencies

```bash
$ pip install -r requirements.txt
```

## Usage

Just do it.

```
$ python3 download_all_mp3.py
```

This command will start a downloader with 30 threads by default and put the result to download/.

It is also possible to specify:
- How many threads are used
- Which words exactly to download
- Which sources for words are preferred
- Where to put resulting mp3 files

Use help to see full usage.

More advanced example:
```
$ python3 download_all_mp3.py -t 1 -w "apple, banana" --prefer amazon -d my_words
```
This will download mp3 for apple and banana in 1 thread, preferring links with substring "amazon" (usually stands for Oxford Dictionaries).
The result will be stored in my_words directory.


## Use `data.json` and `ultimate.json` in Other Applications

The [data.json](data.json) and [ultimate.json](ultimate.json) file contains the URLs to the pronunciation MP3 audio files for 119,377 unique English words.

My own crawler framework took tens of hours to get all the data from the Web. Now, you can use the data directly free of charge, instead of having to spend your time and effort to write the crawler and to crawl the Web. The idea behind this project is just like [rainbow tables](https://en.wikipedia.org/wiki/Rainbow_table). 

The only difference between [data.json](data.json) and [ultimate.json](ultimate.json) is, the former contains only one URL for each word/term, while the latter have all the URLs that ever appeared in all online dictionaries.

For example, a segment of the `data.json` file looks like:

```json
{
	"abel": "http://static.sfdict.com/staticrep/dictaudio/A00/A0015900.mp3",
	"abele": "http://www.yourdictionary.com/audio/a/ab/abele.mp3",
	"abelia": "http://s3.amazonaws.com/audio.vocabulary.com/1.0/us/A/1IFDVKNEVQTHP.mp3",
	"abelmoschus": "http://img2.tfd.com/pron/mp3/en/US/sh/shdjdgdyslsjsfsodrsksns3h7h3.mp3",
	"abelmosk": "http://img2.tfd.com/pron/mp3/en/UK/dr/drdjdgdyslsjsfsoshgk.mp3",
	"abenaki": "http://img2.tfd.com/pron/mp3/en/US/dt/dtdjdgdysjddskslhn.mp3",
	"aberdare": "http://img2.tfd.com/pron/mp3/en/UK/df/dfdjdgdysddtdsstd7gk.mp3",
	"aberdeen": "http://www.yourdictionary.com/audio/a/ab/aberdeen.mp3"
}
```

While the corresponding segment in `ultimate.json`:

```json
	"abel": [
		"http://static.sfdict.com/staticrep/dictaudio/A00/A0015900.mp3",
		"http://img2.tfd.com/pron/mp3/en/US/d5/d5djdgdyslht.mp3",
		"http://img2.tfd.com/pron/mp3/en/UK/d5/d5djdgdyslht.mp3",
		"http://www.yourdictionary.com/audio/a/ab/abel.mp3"
	],
	"abele": [
		"http://www.yourdictionary.com/audio/a/ab/abele.mp3",
		"http://static.sfdict.com/staticrep/dictaudio/A00/A0016300.mp3",
		"http://www.oxforddictionaries.com/media/english/uk_pron/a/abe/abele/abele__gb_2_8.mp3",
		"http://s3.amazonaws.com/audio.vocabulary.com/1.0/us/A/1B3JGI7ALNB2K.mp3",
		"http://www.oxforddictionaries.com/media/english/uk_pron/a/abe/abele/abele__gb_1_8.mp3"
	],
	"abelia": [
		"http://s3.amazonaws.com/audio.vocabulary.com/1.0/us/A/1IFDVKNEVQTHP.mp3",
		"http://www.oxforddictionaries.com/media/english/uk_pron/a/abe/abeli/abelia__gb_1_8.mp3",
		"http://www.yourdictionary.com/audio/a/ab/abelia.mp3",
		"http://static.sfdict.com/staticrep/dictaudio/A00/A0016400.mp3"
	],
	"abelmoschus": [
		"http://img2.tfd.com/pron/mp3/en/US/sh/shdjdgdyslsjsfsodrsksns3h7h3.mp3"
	],
	"abelmosk": [
		"http://img2.tfd.com/pron/mp3/en/UK/dr/drdjdgdyslsjsfsoshgk.mp3",
		"http://static.sfdict.com/staticrep/dictaudio/A00/A0016700.mp3",
		"http://s3.amazonaws.com/audio.vocabulary.com/1.0/us/A/G9XTJLHSNJWL.mp3"
	],
	"abenaki": [
		"http://img2.tfd.com/pron/mp3/en/US/dt/dtdjdgdysjddskslhn.mp3",
		"http://static.sfdict.com/staticrep/dictaudio/A00/A0016800.mp3",
		"http://www.yourdictionary.com/audio/a/ab/abenaki.mp3"
	],
	"aberdare": [
		"http://img2.tfd.com/pron/mp3/en/UK/df/dfdjdgdysddtdsstd7gk.mp3",
		"http://img2.tfd.com/pron/mp3/en/US/df/dfdjdgdysddtdsstd7gk.mp3",
		"http://static.sfdict.com/staticrep/dictaudio/A00/A0017100.mp3"
	],
	"aberdeen": [
		"http://www.yourdictionary.com/audio/a/ab/aberdeen.mp3",
		"http://static.sfdict.com/staticrep/dictaudio/A00/A0017200.mp3"
	]
```

Apparently, each key is an English word and the value is either the URL, or a list of URLs, to the MP3 audio files.

The `data.json` and `ultimate.json` are 11.1 MB and 39.1 MB respectively, so you can load any of them into the memory and let it serve as a look-up table.

## Acknowledgements

The list of words is downloaded from a third-party distributor of WordNet called [Words API Blog](http://blog.wordsapi.com/2015/01/a-wordnet-word-list.html).

My special thanks to these online dictionary owners for making their websites crawlable. Some of them apparently devoted quite some effort hiding out the MP3 URls from the main HTML files though.
