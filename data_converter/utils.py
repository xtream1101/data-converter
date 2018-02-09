import os
from data_converter import csv_helper
from data_converter import json_helper

supported_file_types = ['json', 'csv']

converters = {'csv': csv_helper,
              'json': json_helper,
              }


def _check_input_file(file, output_type):
    """Check that:
    - the file exists
    - is supported
    - type is not the same as the output type

    Args:
        file (str): path to the file
        output_type (str): file extension without the `.` of the output data

    Returns:
        str: Absolute file path of input file

    Raises:
        FileNotFoundError: If the file does not exists

    """
    output_type = output_type.lower()
    file = _get_absolute_path(file)
    if not os.path.isfile(file):
        raise FileNotFoundError("File does not exists: {file}".format(file=file))

    ext = _get_file_ext(file).lower()
    if not _is_file_ext_supported(ext):
        raise ValueError("This file format is not supported: {ext}".format(ext=ext))

    if ext == output_type:
        raise UserWarning("No need to convert {in_ext}->{out_ext}".format(in_ext=ext, out_ext=output_type))

    return file


def _get_absolute_path(file):
    return os.path.abspath(os.path.expanduser(file))


def rreplace(s, old, new):
    """ Needed to replace file ext

    Args:
        s (str): String to replace the value in
        old (str): string to be replaced
        new (str): string to replace with

    Returns:
        str: The full string with the last occurrence replaced

    """
    li = s.rsplit(old, 1)  # Split only once
    return new.join(li)


def _get_file_ext(file):
    """Get the file extension
    Args:
        file (str): path to the file

    Returns:
        str: file extension without the `.`

    """
    return os.path.splitext(file)[1][1:]  # [1:] removes the `.`


def _is_file_ext_supported(file_ext):
    """Check that the file extension is supported

    Args:
        file_ext (str): file extension without the `.`

    Returns:
        bool: True if the file is suported, else False

    """
    return file_ext.lower() in supported_file_types
