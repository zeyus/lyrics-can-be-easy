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


**Examples**

```
$ python3 lyrics_can_be_easy.py --provider wikia --numlines 30 "Matchbox 20" "Opeth" > lyrics.txt
Cache DB found, using saved data
=====♫♫♫♫♫♫♫♫♫=====




$  cat lyrics.txt
You're like your head around
Morning falls like you
Confessor of pain in seconds of my presence
You left for you know if I turned you
And she wrote down
to my window
Talk like your seclusion
White summer rain, in
And I've got you run
[reversed
Now I can't get
Dead
Calling the way
The last
Aching
I
These matters
Like the quiet moments
By the sill
Enduring yet
And I'm walking behind with shadows on the start to let you go
I had a wound that whole lot
Halting at the words I fall down word you think you
But now
And I said I think you're already leaving
I wrote
Twisted face
Don't you shut down under the vile
Baying behind you wanna believe
Don't it came passing by

$ 
```


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

