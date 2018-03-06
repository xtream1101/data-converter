from openpyxl import load_workbook
from data_converter import utils


def _list_from_xlsx_with_header(wb):
    sheet_data = []

    for sheet in wb:
        headers = [cell.value for cell in sheet.iter_rows(min_row=1, max_row=1).next()]
        sheet_width = len(headers)
        sheet_iterator = sheet.iter_rows(min_row=2)
        # iterate through each sheet_iteartor, and append the headers and row value of index i, from 0 to
        # to width of the sheet (number of columns)
        sheet_data.append({sheet.title: [
            {headers[i]: row[i].value for i in range(sheet_width)}
            for row in sheet_iterator
        ]
        })

    return sheet_data


def _list_from_xlsx_without_header(wb):
    sheet_data = []

    for sheet in wb:
        sheet_iterator = sheet.iter_rows(min_row=1)
        # iterate through each sheet_iteartor, and append the headers and row value of index i, from 0 to
        # to width of the sheet (number of columns)
        sheet_data.append({sheet.title: [
            [cell.value for cell in row]
            for row in sheet_iterator
        ]
        })

    return sheet_data


def read_file(input_file, header=True):
    # data_only returns values in xlsx files rather than formulae
    ext = utils._get_file_ext(input_file)
    if ext != 'xlsx':
        raise ValueError("Expecting a xlsx file, but got: {ext}".format(ext=ext))

    wb = load_workbook(filename=input_file, data_only=True)
    sheet_data = _list_from_xlsx_with_header(wb) if header else _list_from_xlsx_without_header(wb)

    return sheet_data


def write_file():
    pass


if __name__ == "__main__":
    print(read_file("/Users/richard/Desktop/test.xlsx"))
    print(read_file("/Users/richard/Desktop/test.xlsx", header=False))
