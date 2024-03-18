from app.io.input import input_from_console, input_from_file_builtin, input_from_file_pandas
from app.io.output import output_to_file_builtin, output_to_console


def main():
    text_from_console = input_from_console()
    output_to_console(text_from_console)

    filename_builtin = "test.txt"
    text_from_file_builtin = input_from_file_builtin(filename_builtin)
    output_to_file_builtin("output_file.txt", text_from_console)
    output_to_console(text_from_file_builtin)

    filename_pandas = "file_pandas.csv"
    data_from_file_pandas = input_from_file_pandas(filename_pandas)

    # Print contents of file_pandas.csv to console
    print(data_from_file_pandas)

    # Convert DataFrame to CSV-formatted string
    data_as_string = data_from_file_pandas.to_csv(index=False)
    output_to_file_builtin("output_pandas.csv", data_as_string)  # Use output_to_file_builtin for writing string data


if __name__ == "__main__":
    main()
