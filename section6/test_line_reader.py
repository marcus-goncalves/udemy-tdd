"""
USE CASES
- Can call read_from_file
- read_from_file returns correct string
- read_from_files throws exception when file doesn't exist
"""
from .line_reader import read_from_file
from unittest.mock import MagicMock
import pytest


def test_ReturnsCorrectString(monkeypatch) -> None:
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value='test line')

    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    result = read_from_file("blah")

    mock_open.assert_called_once_with("blah", "r")
    assert result == "test line"


def test_ExceptionDoesntExists(monkeypatch) -> None:
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value='test line')

    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)

    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr('os.path.exists', mock_exists)
    with pytest.raises(Exception):
        result = read_from_file('blah')
