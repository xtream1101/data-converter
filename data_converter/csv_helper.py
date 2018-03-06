import csv
from data_converter import utils


def read_file(input_file, has_header=True, **kwargs):
    """Write a list of lists/dics to a csv file

    Args:
        output_data (list): list of lists/dicts of data to be saved

    Named Args:
        has_header (bool): Default `True`. If the csv file has a header
        **kwargs: Catches all other args that were passed but do not care about

    Returns:
        str: Absolute file path of the saved file

    """
    ext = utils._get_file_ext(input_file)
    if ext != 'csv':
        raise ValueError("Expecting a csv file, but got: {ext}".format(ext=ext))

    input_data = None
    with open(utils._get_absolute_path(input_file)) as csv_file:
        if has_header is False:
            input_data = list(csv.reader(csv_file))
        else:
            input_data = []
            for row in csv.DictReader(csv_file):
                # Convert OrderedDict to normal dict
                input_data.append(dict(row))

    return input_data


@utils.create_write_file_object
def write_file(output_data, output_file, has_header=True, **kwargs):
    """Write a list of lists/dics to a csv file

    Args:
        output_data (list): list of lists/dicts of data to be saved
        output_file (str/file): Path to output file. Or filetype object to write the data to

    Named Args:
        has_header (bool): Default `True`. If the csv file has a header
        **kwargs: Catches all other args that were passed but do not care about

    Returns (via @utils._create_file_object):
        str/file: Absolute file path of the saved file or the file object. Depending what was passed in

    """
    if has_header is False or isinstance(output_data[0], (list, tuple)):
        writer = csv.writer(output_file)
        if isinstance(output_data[0], dict):
            # If trying to write a list of dicts, but do not want the header row
            for row in output_data:
                writer.writerow(row.values())
        else:
            writer.writerows(output_data)

    else:
        # Write a lits of dicts with header on first row
        field_names = output_data[0].keys()
        writer = csv.DictWriter(output_file, fieldnames=field_names)
        writer.writeheader()
        for data in output_data:
            writer.writerow(data)
