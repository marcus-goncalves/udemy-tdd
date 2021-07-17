"""
USE CASES
- Can call read_from_file
- read_from_file returns correct string
- read_from_files throws exception when file doesn't exist
"""
from .line_reader import read_from_file


def test_CallReadFromFile() -> None:
    read_from_file("blac")
