import os
import argparse
from data_converter import utils


def convert(input_file, to_format):
    """Convert input_file into another format

    Raises:
        FileNotFoundError & UserWarning: from the function `_check_input_file`
        ValueError

    Returns:
        str: Absolute file path of output file

    """
    if not utils._is_file_ext_supported(to_format):
        raise ValueError("File extension is not supported: {ext}".format(ext=to_format))

    input_file = utils._check_input_file(input_file, to_format)
    input_ext = utils._get_file_ext(input_file)

    # Read in data
    input_data = converters[input_ext].read_file(input_file)

    # Write out data
    output_file = utils.rreplace(input_file, input_ext, to_format)
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
