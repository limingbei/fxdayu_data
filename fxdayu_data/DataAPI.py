# encoding:utf-8


__all__ = ["init_config", "set_file", "candle", "factor", "get"]
FILE = 'config.py'


def exec_config_file():
    try:
        execfile(FILE, globals())
    except NameError:
        exec(open(FILE).read(), globals())


def init_config():
    try:
        exec_config_file()
    except IOError as ioe:
        print(ioe)
        return


def set_file(file_path):
    global FILE
    FILE = file_path
    init_config()


def candle(symbols, freq, fields=None, start=None, end=None, length=None, adjust=None):
    """

    :param symbols: str | tuple(str) | hashable array
    :param freq:  str
    :param fields: str | tuple(str) | hashable array
    :param start: datetime.datetime
    :param end: datetime.datetime
    :param length: int
    :param adjust: str | None
    :return: pd.DataFrame or pd.Panel
    """
    pass


def factor(symbols, fields, start=None, end=None, length=None):
    """

    :param symbols: str | tuple(str) | hashable array
    :param fields: str | tuple(str) | hashable array
    :param start: datetime.datetime
    :param end: datetime.datetime
    :param length: int
    :return: pd.DataFrame or pd.Panel
    """
    pass


def get(api, *args, **kwargs):
    return globals()[api](*args, **kwargs)


init_config()