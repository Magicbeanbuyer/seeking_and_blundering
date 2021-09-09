from src import simple_etl
from unittest.mock import mock_open, patch


def test_read_number_from_file():
    with patch("builtins.open", mock_open(read_data=b"15")) as mock:
        assert simple_etl.read_number_from_file("/fake/path/number.txt") == 15
        mock.assert_called_once_with("/fake/path/number.txt", mode="rb")


def test_double_number():
    assert simple_etl.double_number(2) == 4


def test_save_number():
    my_mock = mock_open()
    with patch("builtins.open", my_mock):
        simple_etl.save_number(100, "/fake/path/number.txt")
        my_mock.assert_called_once_with("/fake/path/number.txt", mode="w")
        my_mock().write.assert_called_once_with("100")
