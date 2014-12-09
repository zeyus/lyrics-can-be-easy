from abc import ABCMeta, abstractmethod

class ApiBase(object, metaclass=ABCMeta):
    api_endpoint = ""
    _api_key = ""

    @abstractmethod
    def get_lyrics(self, artist):
        pass

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, val):
        self._api_key = val