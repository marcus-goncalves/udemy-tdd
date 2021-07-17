import os

from _pytest.python_api import raises


def read_from_file(filename: str) -> str:
    if not os.path.exists(filename):
        raise Exception("Bad file")

    infile = open(filename, 'r')
    line = infile.readline()
    return line
