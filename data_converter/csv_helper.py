import csv
from data_converter import utils


def read_file(input_file):
    """
    """
    ext = utils._get_file_ext(input_file)
    if ext != 'csv':
        raise ValueError("Expecting a csv file, but got: {ext}".format(ext=ext))

    input_data = None
    with open(utils._get_absolute_path(input_file)) as csv_file:
        input_data = list(csv.DictReader(csv_file))

    return input_data


def write_file(output_data, output_file):
    with open(output_file, 'w') as csv_file:
        field_names = output_data[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        for data in output_data:
            writer.writerow(data)

