#!/usr/bin/env python3

from pymarkovchain import MarkovChain
import urllib.request
import json
from urllib.parse import urlencode
import os
import sys
import re
import argparse
import hashlib

def check_minvalue(value):
    ivalue = int(value)
    if ivalue < 1:
         raise argparse.ArgumentTypeError("%s needs to be at least 1" % value)
    return ivalue

parser = argparse.ArgumentParser(description='Generate random song lyrics based on an artist/group\'s vocabulary')
parser.add_argument('artist', metavar='"Artist"', type=str, nargs='+',
                    help='Artist(s) to base dictionary on')
parser.add_argument('--key', help='API key for lyricsnmusic.com', required=True)

parser.add_argument('--numlines', help='number of "sentences" to generate', required=False, type=check_minvalue, default=5)

args = parser.parse_args()

sorted_artists = [x.lower() for x in args.artist]
sorted_artists = sorted(sorted_artists)

cache_db_name = hashlib.md5(' '.join(sorted_artists).encode('utf-8')).hexdigest()
mc = MarkovChain(cache_db_name)
if not os.path.isfile(cache_db_name):
    print('No cache DB found, generating', file=sys.stderr)
    for artist in sorted_artists:
        print('Retrieving song data for "{}" from api.lyricsnmusic.com'.format(artist), file=sys.stderr)
        uri = "http://api.lyricsnmusic.com/songs?{}"
        params = {
            'api_key': args.key,
            'artist': artist,
        }

        uri = uri.format(urlencode(params))

        response = urllib.request.urlopen(uri)
        songdata = json.loads(response.read().decode('utf-8'))

        all_lyrics = ''
        for song in songdata:
            snip = re.sub(r'(\[[^\]]+\])|(\s[^\s\.]*\.\.\.\s*$)', '', song['snippet'])

            all_lyrics = all_lyrics + snip + '\r\n'
    print('Saving DB...', file=sys.stderr)
    mc.generateDatabase(all_lyrics)
    mc.dumpdb()
else:
    print('Cache DB found, using saved data', file=sys.stderr)

print('=====♫♫♫♫♫♫♫♫♫=====\n\n\n', file=sys.stderr)

for i in range(0, args.numlines):
    print(mc.generateString())