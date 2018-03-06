import os

supported_file_types = ['json', 'csv', 'xlsx']


def _chunks_of(max_chunk_size, list_to_chunk):
    """Yields the list with a max size of max_chunk_size

    Args:
        max_chunk_size (int): Max rows a chunk can be
        list_to_chunk (list): List to break up into smaller chunks

    Yields:
        list: list of data with a max length max_chunk_size

    """
    for i in range(0, len(list_to_chunk), max_chunk_size):
        yield list_to_chunk[i:i + max_chunk_size]


def create_write_file_object(func):
    """Decorator for when writing data to files
    """
    def wrapper(*args, **kwargs):
        """Takes the file passed in an converts it to a file type object of needed
        Then writes the data to the file

        Args:
            0 (list of dicts): Dtaa to be saved
            1 (str/file object): File to save the data to

        Returns:
            str/file object: If data is not being chunked
            list of str/file object: If data is being chunked up

        """
        args = list(args)
        file = args[1]

        chunk_size = kwargs.get('chunk_size', None)

        if isinstance(file, str):
            is_file_path = True
        elif hasattr(file, 'write'):
            is_file_path = False
        else:
            raise ValueError("Invalid file path or object")

        if chunk_size is None:
            if is_file_path is True:
                # Create a file object if one was not passed in
                file = _get_absolute_path(file)
                save_file = open(file, 'w')
            else:
                save_file = file

            args[1] = save_file
            kwargs['file_path'] = file  # Just so the function still has access to the original file name
            func(*args, **kwargs)

            if is_file_path is True:
                save_file.close()
                output = file
            else:
                output = save_file

        else:
            # Chunk up the file
            output = []
            for i, chunk in enumerate(_chunks_of(chunk_size, args[0]), start=1):
                if is_file_path is True:
                    # Create a file object if one was not passed in
                    full_path = _get_absolute_path(file)
                    ext = '.' + _get_file_ext(file)
                    save_file_name = full_path.replace(ext, '_' + str(i) + ext)
                    kwargs['file_path'] = full_path  # Just so the function still has access to the original file name
                    save_file = open(save_file_name, 'w')
                else:
                    kwargs['file_path'] = file  # Just so the function still has access to the original file name
                    save_file = file.copy()

                args[0] = chunk
                args[1] = save_file
                func(*args, **kwargs)

                if is_file_path is True:
                    save_file.close()
                    output.append(save_file_name)
                else:
                    output.append(save_file)

        return output

    return wrapper


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
    """Gets the absolute path of a file path

    Args:
        file (str): File path as string

    Returns:
        str: Full expanded path to file

    """
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
