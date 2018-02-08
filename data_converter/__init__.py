import os
import argparse
from data_converter import csv_helper
from data_converter import json_helper


def cli():
    """Command line tool to convert data file into other formats

    Notes:
        Not using pathlib because trying to keep this as compatible as posiable with other versions

    """
    parser = argparse.ArgumentParser(description='Convert data files')
    parser.add_argument('-t', '--to', help='Format to convert to', required=True)
    parser.add_argument('input_file', help='File to convert from')

    args = parser.parse_args()

    input_file = os.path.abspath(os.path.expanduser(args.input_file))
    input_file_type = os.path.splitext(input_file)[1][1:]

    read_data = {'csv': csv_helper.read_file,
                 'json': json_helper.read_file,
                 }
    write_data = {'csv': csv_helper.write_file,
                  'json': json_helper.write_file,
                  }

    # Read in data
    input_data = read_data[input_file_type](input_file)

    # Write out data
    output_file_type = args.to
    output_file = input_file.replace(input_file_type, output_file_type)
    write_data[output_file_type](input_data, output_file)

    print(output_file)
