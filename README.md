Lyrics can be easy
===================

Have you hit the edge of your creativity? Writing music got you down? Want to sound like your favourite artists? 

Enter 'lyrics can be easy,' your one stop lyrics production shop.

Using python 3 and the wonderful 'pymarkovchain' in conjunction with http://api.lyricsnmusic.com/ this script is incredibly small and fairly fast.

**How it works**

The snippet of lyrics is pulled via the API (unfortunately just a "preview" but it would be easy to integrate this into other services) and then fed into the markov chain generator to print out a line or lines of pseudo-lyrics

**APIs**

Currently support:

- lyricsnmusic api (get key here: http://www.lyricsnmusic.com/api_keys/new)
- wikia lyrics api (documentation here: http://api.wikia.com/wiki/LyricWiki_API)

default is lyricsnmusic.

**known issues**

Full lyrics cannot be retrieved from free API service, so you'll have to live with 1/7th of the song :(


**Requirements**

- pymarkovchain

```pip install pymarkovchain```

**Usage**

```
./lyrics_can_be_easy.py -h
```

outputs:
```
usage: lyrics_can_be_easy.py [-h] [--key KEY]
                             [--provider {lyricsnmusic,wikia}]
                             [--numlines NUMLINES]
                             "Artist" ["Artist" ...]

Generate random song lyrics based on an artist/group's vocabulary

positional arguments:
  "Artist"              Artist(s) to base dictionary on

optional arguments:
  -h, --help            show this help message and exit
  --key KEY             API key if using lyricsnmusic.com
  --provider {lyricsnmusic,wikia}
                        API provider
  --numlines NUMLINES   number of "sentences" to generate
```


**Example**

```
$ ./lyrics_can_be_easy.py --numlines 10  --key abcdefg1234567890 "tool" "a perfect circle"

Cache DB found, using saved data
=====♫♫♫♫♫♫♫♫♫=====



Puzzled and higher ground,
How we come in
I hold now, so I hold now
Suck
What is near
snatching me on a box of Area 51
Feast like a sultan I wouldn't have a test
Looking to say the ocean"
Looking for a snake
Boredom's not a vacation from my infancy
```

