#!/usr/bin/env python3

from pymarkovchain import MarkovChain
import os
import sys
import argparse
import hashlib
from lyricapis.wikia import wikia
from lyricapis.lyricsnmusic import lyricsnmusic


def check_minvalue(value):
    ivalue = int(value)
    if ivalue < 1:
        raise argparse.ArgumentTypeError("%s needs to be at least 1" % value)
    return ivalue


parser = argparse.ArgumentParser(description='Generate random song lyrics based on an artist/group\'s vocabulary')
parser.add_argument('artist', metavar='"Artist"', type=str, nargs='+',
                    help='Artist(s) to base dictionary on')
parser.add_argument('--key', help='API key if using lyricsnmusic.com', required=False, default=None)
parser.add_argument('--provider', help='API provider', required=False, default='lyricsnmusic',
                    choices=['lyricsnmusic', 'wikia'])

parser.add_argument('--numlines', help='number of "sentences" to generate', required=False, type=check_minvalue,
                    default=5)

args = parser.parse_args()

sorted_artists = [x.lower() for x in args.artist]
sorted_artists = sorted(sorted_artists)

cache_db_name = hashlib.md5(' '.join(sorted_artists).encode('utf-8') + args.provider.encode('utf-8')).hexdigest()

target_api = globals()[args.provider]
lyrical_api = target_api()

if not args.key is None:
    lyrical_api.api_key = args.key


mc = MarkovChain(cache_db_name)
if not os.path.isfile(cache_db_name):
    print('No cache DB found, generating', file=sys.stderr)
    all_lyrics = ''
    for artist in sorted_artists:
        print('Retrieving song data for "{}" from {}.'.format(artist, args.provider), file=sys.stderr)
        all_lyrics += lyrical_api.get_lyrics(artist)

    print('Saving DB...', file=sys.stderr)
    mc.generateDatabase(all_lyrics)
    mc.dumpdb()
else:
    print('Cache DB found, using saved data', file=sys.stderr)

print('=====♫♫♫♫♫♫♫♫♫=====\n\n\n', file=sys.stderr)

for i in range(0, args.numlines):
    print(mc.generateString())