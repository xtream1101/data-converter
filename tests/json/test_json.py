import os
import hashlib
import tempfile
import data_converter


def get_file_hash(file):
    return hashlib.md5(open(file).read().strip().encode('utf-8')).hexdigest()


def _get_base_path(file_name):
    return os.path.join('tests', 'json', file_name)


#
# Reads
#
def test_json_read_list_of_dicts():
    content = [{'a': 1, 'b': 'bee', 'c': 3.14},
               {'a': 2, 'b': 'butterfly', 'c': 6.28}]
    assert data_converter.json_helper.read_file(_get_base_path('list_of_dicts.json')) == content


def test_json_read_list_of_dicts_mixed_keys():
    content = [{'a': 1, 'b': 'bee', 'c': 3.14},
               {'d': 2, 'e': 'butterfly', 'c': 6.28}]
    assert data_converter.json_helper.read_file(_get_base_path('list_of_dicts_mixed_keys.json')) == content


def test_json_read_list_of_lists():
    content = [[1, 'bee', 3.14],
               [2, 'butterfly', 6.28]]
    assert data_converter.json_helper.read_file(_get_base_path('list_of_lists.json')) == content


#
# Writes
#
def test_output_return_is_path():
    content = [{'a': 1, 'b': 'bee', 'c': 3.14},
               {'a': 2, 'b': 'butterfly', 'c': 6.28}]
    with tempfile.NamedTemporaryFile() as f:
        tmp_file = data_converter.json_helper.write_file(content, f.name)

    assert isinstance(tmp_file, str)


def test_output_return_is_file():
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

    content = [{'a': 1, 'b': 'bee', 'c': 3.14},
               {'a': 2, 'b': 'butterfly', 'c': 6.28}]

    tmp_file = data_converter.json_helper.write_file(content, StringIO())

    assert hasattr(tmp_file, 'write')


def test_json_write_list_of_dicts():
    content = [{'a': 1, 'b': 'bee', 'c': 3.14},
               {'a': 2, 'b': 'butterfly', 'c': 6.28}]
    with tempfile.NamedTemporaryFile(delete=False) as f:
        tmp_file = data_converter.json_helper.write_file(content, f.name)
        tmp_file_hash = get_file_hash(tmp_file)

    assert tmp_file_hash == get_file_hash(_get_base_path('list_of_dicts.json'))


def test_json_write_list_of_dicts_mixed_keys():
    content = [{'a': 1, 'b': 'bee', 'c': 3.14},
               {'d': 2, 'e': 'butterfly', 'c': 6.28}]
    with tempfile.NamedTemporaryFile(delete=False) as f:
        tmp_file = data_converter.json_helper.write_file(content, f.name)
        tmp_file_hash = get_file_hash(tmp_file)

    assert tmp_file_hash == get_file_hash(_get_base_path('list_of_dicts_mixed_keys.json'))


def test_json_write_list_of_lists():
    content = [[1, 'bee', 3.14],
               [2, 'butterfly', 6.28]]
    with tempfile.NamedTemporaryFile(delete=False) as f:
        tmp_file = data_converter.json_helper.write_file(content, f.name)
        tmp_file_hash = get_file_hash(tmp_file)

    assert tmp_file_hash == get_file_hash(_get_base_path('list_of_lists.json'))
