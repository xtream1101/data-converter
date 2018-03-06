import os
import pytest
import hashlib
import tempfile
import data_converter


def get_file_hash(file):
    return hashlib.md5(open(file).read().strip().encode('utf-8')).hexdigest()


def _get_base_path(file_name):
    return os.path.join('tests', 'csv', file_name)


#
# Reads
#
def test_csv_read_dict_with_headers():
    content = [{'a': '1', 'b': 'bee', 'c': '3.14'},
               {'a': '2', 'b': 'butterfly', 'c': '6.28'}]
    assert data_converter.csv_helper.read_file(_get_base_path('csv_with_header.csv')) == content


def test_csv_read_list_no_headers():
    content = [['1', 'bee', '3.14'],
               ['2', 'butterfly', '6.28']]
    test_file = _get_base_path('csv_no_header.csv')
    assert data_converter.csv_helper.read_file(test_file, has_header=False) == content


#
# Writes
#
def test_output_chunk_1_line_each():
    content = [{'a': 1, 'b': 'bee', 'c': 3.14},
               {'a': 2, 'b': 'butterfly', 'c': 6.28}]

    file_hashes = []
    tmp_files = data_converter.csv_helper.write_file(content, 'test_csv_chunk_of_1.csv', chunk_size=1)
    for tmp_file in tmp_files:
        file_hashes.append(get_file_hash(tmp_file))
        os.remove(tmp_file)

    assert file_hashes[0] == get_file_hash(_get_base_path('chunk_1_of_2.csv'))
    assert file_hashes[1] == get_file_hash(_get_base_path('chunk_2_of_2.csv'))


def test_output_return_is_path():
    content = [{'a': 1, 'b': 'bee', 'c': 3.14},
               {'a': 2, 'b': 'butterfly', 'c': 6.28}]
    with tempfile.NamedTemporaryFile() as f:
        tmp_file = data_converter.csv_helper.write_file(content, f.name)

    assert isinstance(tmp_file, str)


def test_output_return_is_file():
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

    content = [{'a': 1, 'b': 'bee', 'c': 3.14},
               {'a': 2, 'b': 'butterfly', 'c': 6.28}]

    tmp_file = data_converter.csv_helper.write_file(content, StringIO())

    assert hasattr(tmp_file, 'write')


def test_csv_write_dict_with_headers():
    content = [{'a': 1, 'b': 'bee', 'c': 3.14},
               {'a': 2, 'b': 'butterfly', 'c': 6.28}]
    with tempfile.NamedTemporaryFile() as f:
        tmp_file = data_converter.csv_helper.write_file(content, f.name)
        tmp_file_hash = get_file_hash(tmp_file)

    assert tmp_file_hash == get_file_hash(_get_base_path('csv_with_header.csv'))


def test_csv_write_dict_with_headers_diff_keys():
    content = [{'a': 1, 'b': 'bee', 'c': 3.14},
               {'a': 2, 'd': 'butterfly', 'c': 6.28}]
    with tempfile.NamedTemporaryFile() as f:
        with pytest.raises(ValueError):
            data_converter.csv_helper.write_file(content, f.name)


def test_csv_write_dict_no_headers():
    content = [{'a': 1, 'b': 'bee', 'c': 3.14},
               {'a': 2, 'b': 'butterfly', 'c': 6.28}]
    with tempfile.NamedTemporaryFile() as f:
        tmp_file = data_converter.csv_helper.write_file(content, f.name, has_header=False)
        tmp_file_hash = get_file_hash(tmp_file)

    assert tmp_file_hash == get_file_hash(_get_base_path('csv_no_header.csv'))


def test_csv_write_list_no_headers():
    content = [[1, 'bee', 3.14],
               [2, 'butterfly', 6.28]]
    with tempfile.NamedTemporaryFile() as f:
        tmp_file = data_converter.csv_helper.write_file(content, f.name, has_header=False)
        tmp_file_hash = get_file_hash(tmp_file)

    assert tmp_file_hash == get_file_hash(_get_base_path('csv_no_header.csv'))


def test_csv_write_list_with_headers_enabled():
    content = [[1, 'bee', 3.14],
               [2, 'butterfly', 6.28]]
    with tempfile.NamedTemporaryFile() as f:
        tmp_file = data_converter.csv_helper.write_file(content, f.name)
        tmp_file_hash = get_file_hash(tmp_file)

    assert tmp_file_hash == get_file_hash(_get_base_path('csv_no_header.csv'))


def test_csv_write_list_with_headers_in_row():
    content = [['a', 'b', 'c'],
               [1, 'bee', 3.14],
               [2, 'butterfly', 6.28]]
    with tempfile.NamedTemporaryFile() as f:
        tmp_file = data_converter.csv_helper.write_file(content, f.name)
        tmp_file_hash = get_file_hash(tmp_file)

    assert tmp_file_hash == get_file_hash(_get_base_path('csv_with_header.csv'))
