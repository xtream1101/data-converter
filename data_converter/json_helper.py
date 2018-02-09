import json
from data_converter import utils


def read_file(input_file):
    """
    """
    ext = utils._get_file_ext(input_file)
    if ext != 'json':
        raise ValueError("Expecting a json file, but got: {ext}".format(ext=ext))

    input_data = None
    with open(utils._get_absolute_path(input_file)) as json_data:
        input_data = json.load(json_data)

    return input_data


def write_file(output_data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(output_data, json_file)

