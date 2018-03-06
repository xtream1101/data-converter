import os

supported_file_types = ['json', 'csv']


def _create_file_object(action, file_index):
    """

    Args:
        action (str): Either read or write, used to check the object attributes
        file_index (int): The index of the file arg to work with
    """
    if action == 'write':
        action_attr = 'write'
        action_open = 'w'
    else:
        action_attr = 'read'
        action_open = 'r'

    def decorator(func):
        """
        """
        def wrapper(*args, **kargs):
            args = list(args)
            file = args[file_index]

            if isinstance(file, str):
                is_file_path = True
            elif hasattr(file, action_attr):
                is_file_path = False
            else:
                raise ValueError("Invalid file path or object")

            if is_file_path is True:
                # Create a file object if one was not passed in
                file = _get_absolute_path(file)
                save_file = open(file, action_open)
            else:
                save_file = file

            args[file_index] = save_file
            func(*args, **kargs)

            if is_file_path is True:
                save_file.close()
                return file

            return save_file

        return wrapper
    return decorator


def _check_input_file(file, output_type):
    """Check that:
    - the file exists
    - is supported
    - type is not the same as the output type

    Args:
        file (str): path to the file
        output_type (str): file extension without the `.` of the output data

    Returns:
        str: Absolute file path of input file

    Raises:
        FileNotFoundError: If the file does not exists

    """
    output_type = output_type.lower()
    file = _get_absolute_path(file)
    if not os.path.isfile(file):
        raise FileNotFoundError("File does not exists: {file}".format(file=file))

    ext = _get_file_ext(file).lower()
    if not _is_file_ext_supported(ext):
        raise ValueError("This file format is not supported: {ext}".format(ext=ext))

    if ext == output_type:
        raise UserWarning("No need to convert {in_ext}->{out_ext}".format(in_ext=ext, out_ext=output_type))

    return file


def _get_absolute_path(file):
    return os.path.abspath(os.path.expanduser(file))


def rreplace(s, old, new):
    """ Needed to replace file ext

    Args:
        s (str): String to replace the value in
        old (str): string to be replaced
        new (str): string to replace with

    Returns:
        str: The full string with the last occurrence replaced

    """
    li = s.rsplit(old, 1)  # Split only once
    return new.join(li)


def _get_file_ext(file):
    """Get the file extension
    Args:
        file (str): path to the file

    Returns:
        str: file extension without the `.`

    """
    return os.path.splitext(file)[1][1:]  # [1:] removes the `.`


def _is_file_ext_supported(file_ext):
    """Check that the file extension is supported

    Args:
        file_ext (str): file extension without the `.`

    Returns:
        bool: True if the file is suported, else False

    """
    return file_ext.lower() in supported_file_types
