from .base import ApiBase

import urllib.request
import json
from urllib.parse import urlencode
import re

class wikia(ApiBase):
    api_endpoint = "http://lyrics.wikia.com/api.php?fmt=realjson&"

    def get_lyrics(self, artist):
        params = {
            'artist': artist,
        }

        uri = self.api_endpoint + urlencode(params)

        response = urllib.request.urlopen(uri)

        artist_data = json.loads(response.read().decode('utf-8'))

        all_lyrics = ''
        for album in artist_data['albums']:
            for song in album['songs']:
                param = {
                    'song': song
                }
                print('Getting lyrics for song {} from wikia'.format(song))
                response = urllib.request.urlopen(uri + '&' + urlencode(param))
                data = response.read().decode('utf-8')
                song_data = json.loads(data)


                snip = re.sub(r'(\s[^\s\.]*\[\.\.\.\]\s*$)', '', song_data['lyrics'])

                all_lyrics = all_lyrics + snip + '\r\n'

        return all_lyrics