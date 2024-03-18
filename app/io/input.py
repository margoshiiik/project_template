import pandas as pd


def input_from_console():
    """
    Function to input text from the console.

    Returns:
    str: The entered text.
    """
    return input("Enter text from the console: ")


def input_from_file_builtin(filename):
    """
    Function to read text from a file using Python's built-in capabilities.

    Args:
    filename (str): The path to the file.

    Returns:
    str: The content of the file.
    """
    with open(filename, 'r') as file:
        data = file.read()
    return data


def input_from_file_pandas(filename):
    """
    Function to read data from a CSV file using the pandas library.

    Args:
    filename (str): The path to the CSV file.

    Returns:
    pandas.DataFrame: A DataFrame object with the data from the file.
    """
    data = pd.read_csv(filename)
    return data
