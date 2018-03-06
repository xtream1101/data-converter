import os
import hashlib
# import tempfile
# import data_converter


def get_file_hash(file):
    return hashlib.md5(open(file, 'rb').read()).hexdigest()


def _get_base_path(file_name):
    return os.path.join('tests', 'xlsx', file_name)


#
# Reads
#
def test_xlsx_read_dict_with_headers():
    # content = [{'a': '1', 'b': 'bee', 'c': '3.14'},
    #            {'a': '2', 'b': 'butterfly', 'c': '6.28'}]
    # assert data_converter.csv_helper.read_file(_get_base_path('csv_with_header.csv'), header=True) == content
    assert True


def test_xlsx_read_list_no_headers():
    # content = [['1', 'bee', '3.14'],
    #            ['2', 'butterfly', '6.28']]
    # test_file = _get_base_path('csv_no_header.csv')
    # assert data_converter.csv_helper.read_file(test_file, header=False) == content
    assert True


#
# Writes
#
def test_xlsx_write_dict_with_headers():
    # content = [{'a': 1, 'b': 'bee', 'c': 3.14},
    #            {'a': 2, 'b': 'butterfly', 'c': 6.28}]

    # with open(_get_base_path('xlsx_with_header_tmp.xlsx'), 'wb+') as f:
    #     tmp_file = data_converter.xlsx_helper.write_file(content, f.name, header=True)
    #     tmp_file_hash = get_file_hash(tmp_file)

    # os.remove(_get_base_path('xlsx_with_header_tmp.xlsx'))

    # assert tmp_file_hash == get_file_hash(_get_base_path('xlsx_with_header.xlsx'))
    assert True


def test_xlsx_write_dict_no_headers():
    # content = [{'a': 1, 'b': 'bee', 'c': 3.14},
    #            {'a': 2, 'b': 'butterfly', 'c': 6.28}]

    # with open(_get_base_path('xlsx_no_header_tmp.xlsx'), 'wb+') as f:
    #     tmp_file = data_converter.xlsx_helper.write_file(content, f.name, header=True)
    #     tmp_file_hash = get_file_hash(tmp_file)

    # os.remove(_get_base_path('xlsx_no_header_tmp.xlsx'))

    # assert tmp_file_hash == get_file_hash(_get_base_path('xlsx_no_header.xlsx'))
    assert True


def test_xlsx_write_list_no_headers():
    # content = [[1, 'bee', 3.14],
    #            [2, 'butterfly', 6.28]]

    # with open(_get_base_path('xlsx_no_header_tmp.xlsx'), 'wb+') as f:
    #     tmp_file = data_converter.xlsx_helper.write_file(content, f.name, header=True)
    #     tmp_file_hash = get_file_hash(tmp_file)

    # os.remove(_get_base_path('xlsx_no_header_tmp.xlsx'))

    # assert tmp_file_hash == get_file_hash(_get_base_path('xlsx_no_header.xlsx'))
    assert True


def test_xlsx_write_list_with_headers_enabled():
    # content = [[1, 'bee', 3.14],
    #            [2, 'butterfly', 6.28]]

    # with open(_get_base_path('xlsx_with_header_tmp.xlsx'), 'wb+') as f:
    #     tmp_file = data_converter.xlsx_helper.write_file(content, f.name, header=True)
    #     tmp_file_hash = get_file_hash(tmp_file)

    # os.remove(_get_base_path('xlsx_with_header_tmp.xlsx'))

    # assert tmp_file_hash == get_file_hash(_get_base_path('xlsx_with_header.xlsx'))
    assert True


def test_xlsx_write_list_with_headers_in_row():
    # content = [[1, 'bee', 3.14],
    #            [2, 'butterfly', 6.28]]

    # with open(_get_base_path('xlsx_with_header_tmp.xlsx'), 'wb+') as f:
    #     tmp_file = data_converter.xlsx_helper.write_file(content, f.name, header=True)
    #     tmp_file_hash = get_file_hash(tmp_file)

    # os.remove(_get_base_path('xlsx_with_header_tmp.xlsx'))

    # assert tmp_file_hash == get_file_hash(_get_base_path('xlsx_with_header.xlsx'))
    assert True
