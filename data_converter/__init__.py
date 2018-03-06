import sys
import argparse
from data_converter import utils
from data_converter import csv_helper
from data_converter import json_helper
from data_converter import xlsx_helper

converters = {'csv': csv_helper,
              'json': json_helper,
              }


def convert(input_file, to, output_file=None):
    """Convert input_file into another format

    Args:
        input_file (str): File path of the file to convert
        to (str): Format to convert the file to

    Keyword Args:
        output_file (str): Where to save the converted data to, if None it wil output to stdout

    Raises:
        FileNotFoundError & UserWarning: from the function `_check_input_file`
        ValueError

    Returns:
        str: Absolute file path of output file

    """
    if not utils._is_file_ext_supported(to):
        raise ValueError("File extension is not supported: {ext}".format(ext=to))

    input_file = utils._check_input_file(input_file, to)
    input_ext = utils._get_file_ext(input_file)

    # Read in data
    input_data = converters[input_ext].read_file(input_file)

    # Write out data
    if output_file is None:
        # If not output path is set (not even a blank one), the stream the data to stdout
        output_file = sys.stdout
    elif output_file.strip() == '':
        # If blank string, then output the file to the same path as the input just with the new ext
        output_file = utils.rreplace(input_file, input_ext, to)

    return converters[to].write_file(input_data, output_file)


def cli():
    """Command line tool to convert data file into other formats

    Notes:
        Not using pathlib because trying to keep this as compatible as posiable with other versions

    """
    parser = argparse.ArgumentParser(description='Convert data files')
    parser.add_argument('-i', '--input-file', help='File to convert', required=True)
    parser.add_argument('-t', '--to', help='Output format', required=True)
    parser.add_argument('-o', '--output-file', help='Output file', nargs='?')
    args = parser.parse_args()

    try:
        output = convert(args.input_file, args.to, args.output_file)
        if isinstance(output, str):
            # Only print the output if it is the file path, not a file object
            print(output)
    except (FileNotFoundError, UserWarning, ValueError) as e:
        parser.error(str(e))
