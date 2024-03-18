import pandas as pd


def output_to_console(text):
    """
    Function to output text to the console.

    Args:
    text (str): The text to be output.
    """
    print(text)


def output_to_file_builtin(filename, data):
    """
    Function to write data to a file using Python's built-in capabilities.

    Args:
    filename (str): The path to the file.
    data (str): The data to be written.

    Raises:
    TypeError: If the data type is not supported.
    """
    if not isinstance(data, str):
        raise TypeError("Unsupported data type. Expected str.")

    with open(filename, 'w') as file:
        file.write(data)


def output_to_file_pandas(filename, data):
    """
    Function to write data to a file in CSV format using the pandas library.

    Args:
    filename (str): The path to the CSV file.
    data (pandas.DataFrame): The data to be written.
    """
    data.to_csv(filename, index=False)
