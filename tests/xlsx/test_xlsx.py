import datetime
import os
from data_converter import xlsx_helper as x
from expected_outputs import (OUTPUT_LIST, SHEET1, SHEET2, HEADERLESS_OUTPUT_LIST,
                              HEADERLESS_SHEET1, HEADERLESS_SHEET2)

def _get_base_path(file_name):
    return os.path.join('tests', 'xlsx', file_name)

def test_read_xlsx_with_header():
    assert x.read_file(_get_base_path('test.xlsx')) == OUTPUT_LIST

def test_read_xlsx_without_header():
    assert x.read_file(_get_base_path('test.xlsx'),header=False) == HEADERLESS_OUTPUT_LIST
