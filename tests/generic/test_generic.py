import pytest
import data_converter


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        data_converter.csv_helper.read_file('foo_bar.csv')
