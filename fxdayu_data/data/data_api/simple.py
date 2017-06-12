# encoding:utf-8
from fxdayu_data.data.data_api import BasicConfig, lru_cache
from fxdayu_data.data.data_api.tools import ensure_index


class Simple(BasicConfig):

    def __init__(self):
        self.handler = None

    def set(self, handler, db):
        self.handler = handler[db]

    def get(self):
        return self.handler


class Fundamental(Simple):

    def __init__(self):
        super(Fundamental, self).__init__()
        self.indexer = ensure_index('datetime')

    @lru_cache(128)
    def __call__(self, symbols, fields=None, start=None, end=None, length=None):
        return self.handler.read(symbols, start=start, end=end, length=length, projection=self.indexer(fields))