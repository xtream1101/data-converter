import csv


def read_file(input_file):
    """
    """
    input_data = None
    with open(input_file) as csv_file:
        input_data = list(csv.DictReader(csv_file))

    return input_data


def write_file(output_data, output_file):
    with open(output_file, 'w') as csv_file:
        field_names = output_data[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        for data in output_data:
            writer.writerow(data)

