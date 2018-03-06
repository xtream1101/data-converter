from data_converter import utils
from pyexcelerate import Workbook


def read_file(input_file, has_header=True, **kwargs):
    return True


@utils.create_write_file_object
def write_file(output_data, output_file, has_header=True, **kwargs):
    """Write a list of lists/dics to an excel file

    Args:
        output_data (list): list of lists/dicts of data to be saved
        output_file (str): Path to xlsx file

    Named Args:
        **kwargs: Catches all other args that were passed but do not care about

    Returns:
        str: Absolute file path of the saved file

    """
    # if it's a list of lists, just write it to the workbook
    if isinstance(output_data[0], (list, tuple)):
        wb = Workbook()
        wb.new_sheet("Sheet1", data=output_data)
        wb.save(kwargs['file_path'])

    # if it's a list of dicts more logic
    else:
        # convert list of dicts to list of lists
        output = [d.values() for d in output_data]

        # if they want a header, create it from the dict keys
        if has_header:
            output[0:0] = [output_data[0].keys()]

        wb = Workbook()
        wb.new_sheet("Sheet1", data=output)
        wb.save(kwargs['file_path'])
