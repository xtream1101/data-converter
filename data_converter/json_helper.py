import json
from data_converter import utils


def read_file(input_file, **kwargs):
    """Write a list of lists/dics to a json file

    Args:
        output_data (list): list of lists/dicts of data to be saved

    Named Args:
        **kwargs: Catches all other args that were passed but do not care about

    Returns:
        str: Absolute file path of the saved file

    """
    ext = utils._get_file_ext(input_file)
    if ext != 'json':
        raise ValueError("Expecting a json file, but got: {ext}".format(ext=ext))

    input_data = None
    with open(utils._get_absolute_path(input_file)) as json_data:
        input_data = json.load(json_data)

    return input_data


@utils._create_file_object('write', 1)
def write_file(output_data, output_file, **kwargs):
    """Write a list of lists/dics to a json file

    Args:
        output_data (list): list of lists/dicts of data to be saved
        output_file (str/file): Path to output file. Or filetype object to write the data to

    Named Args:
        **kwargs: Catches all other args that were passed but do not care about

    Returns (via @utils._create_file_object)::
        str/file: Absolute file path of the saved file or the file object. Depending what was passed in

    """
    json.dump(output_data, output_file)
