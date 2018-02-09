import os
import argparse
from data_converter import csv_helper
from data_converter import json_helper


supported_file_types = ['json', 'csv']

converters = {'csv': csv_helper,
              'json': json_helper,
              }


def rreplace(s, old, new):
    """ Needed to replace file ext
    TODO: add args to doc string

    """
    li = s.rsplit(old, 1)  # Split only once
    return new.join(li)


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
    file = os.path.abspath(os.path.expanduser(file))
    if not os.path.isfile(file):
        raise FileNotFoundError("File does not exists: {file}".format(file=file))

    ext = _get_file_ext(file).lower()
    if not _is_file_ext_supported(ext):
        raise ValueError("This file format is not supported: {ext}".format(ext=ext))

    if ext == output_type:
        raise UserWarning("No need to convert {in_ext}->{out_ext}".format(in_ext=ext, out_ext=output_type))

    return file


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


def convert(input_file, to_format):
    """Convert input_file into another format

    Raises:
        FileNotFoundError & UserWarning: from the function `_check_input_file`
        ValueError

    Returns:
        str: Absolute file path of output file

    """
    if not _is_file_ext_supported(to_format):
        raise ValueError("File extension is not supported: {ext}".format(ext=to_format))

    input_file = _check_input_file(input_file, to_format)
    input_ext = _get_file_ext(input_file)

    # Read in data
    input_data = converters[input_ext].read_file(input_file)

    # Write out data
    output_file = rreplace(input_file, input_ext, to_format)
    converters[to_format].write_file(input_data, output_file)

    return output_file


def cli():
    """Command line tool to convert data file into other formats

    Notes:
        Not using pathlib because trying to keep this as compatible as posiable with other versions

    """
    parser = argparse.ArgumentParser(description='Convert data files')
    parser.add_argument('-t', '--to', help='Output format', required=True)
    parser.add_argument('input_file', help='File to convert')
    args = parser.parse_args()

    try:
        print(convert(args.input_file, args.to))
    except (FileNotFoundError, UserWarning, ValueError) as e:
        parser.error(str(e))
