import os
import data_converter
from expected_outputs import (OUTPUT_LIST, SHEET1, SHEET2, HEADERLESS_OUTPUT_LIST,
                              HEADERLESS_SHEET1, HEADERLESS_SHEET2)


def _get_base_path(file_name):
    return os.path.join('tests', 'xlsx', file_name)


def test_read_xlsx_with_header():
    assert data_converter.xlsx_helper.read_file(_get_base_path('test.xlsx')) == OUTPUT_LIST


def test_read_xlsx_without_header():
    assert data_converter.xlsx_helper.read_file(_get_base_path('test.xlsx'), header=False) == HEADERLESS_OUTPUT_LIST


def test_xlsx_with_header_sheet_vals():
    data = data_converter.xlsx_helper.read_file(_get_base_path('test.xlsx'))
    assert data['Sheet1'] == SHEET1
    assert data["Price's super cool second sheet"] == SHEET2


def test_xlsx_without_header_sheet_vals():
    data = data_converter.xlsx_helper.read_file(_get_base_path('test.xlsx'), header=False)
    assert data['Sheet1'] == HEADERLESS_SHEET1
    assert data["Price's super cool second sheet"] == HEADERLESS_SHEET2
