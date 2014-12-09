from .base import ApiBase

import urllib.request
import json
from urllib.parse import urlencode
import re

class lyricsnmusic(ApiBase):
    api_endpoint = "http://api.lyricsnmusic.com/songs?"

    def get_lyrics(self, artist):
        params = {
            'api_key': self.api_key,
            'artist': artist,
        }

        if not self.api_key:
            raise ValueError('Invalid API key')

        uri = self.api_endpoint + urlencode(params)

        response = urllib.request.urlopen(uri)
        song_data = json.loads(response.read().decode('utf-8'))
        all_lyrics = ''
        for song in song_data:
            snip = re.sub(r'(\[[^\]]+\])|(\s[^\s\.]*\.\.\.\s*$)', '', song['snippet'])

            all_lyrics = all_lyrics + snip + '\r\n'

        return all_lyrics