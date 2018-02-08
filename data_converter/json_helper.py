import json


def read_file(input_file):
    """
    """
    input_data = None
    with open(input_file) as json_data:
        input_data = json.load(json_data)

    return input_data


def write_file(output_data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(output_data, json_file)

