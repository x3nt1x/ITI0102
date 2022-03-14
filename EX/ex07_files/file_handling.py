"""Handle files."""
import csv
import datetime
from pathlib import Path


def read_file_contents(filename: str) -> str:
    """
    Read file contents into string.

    In this exercise, we can assume the file exists.

    :param filename: File to read.
    :return: File contents as string.
    """
    with open(filename) as file:
        return file.read()


def read_file_contents_to_list(filename: str) -> list:
    """
    Read file contents into list of lines.

    In this exercise, we can assume the file exists.
    Each line from the file should be a separate element.

    List elements should not contain new line.

    :param filename: File to read.
    :return: List of lines.
    """
    data = list()

    with open(filename) as file:
        for line in file:
            data.append(line.strip())

    return data


def read_csv_file(filename: str, dlimiter=",") -> list:
    """
    Read CSV file into list of rows.

    Each row is also a list of "columns" or fields.

    CSV (Comma-separated values) example:
    name,age
    john,12
    mary,14

    Should become:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Use csv module.

    :param filename: File to read.
    :param dlimiter: Delimiter.
    :return: List of lists.
    """
    data = list()

    with open(filename) as file:
        for row in csv.reader(file, delimiter=dlimiter):
            data.append(row)

    return data


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to file.

    If the file doesn't exist, create it.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    with open(filename, "w") as file:
        file.write(contents)


def write_lines_to_file(filename: str, lines: list) -> None:
    """
    Write lines to file.

    Lines is a list of strings, each represents a separate line in the file.

    There should be no new line in the end of the file.
    Unless the last element itself ends with the new line.

    :param filename: File to write to.
    :param lines: List of string to write to the file.
    :return: None
    """
    with open(filename, "w") as file:
        file.write('\n'.join(lines))


def write_csv_file(filename: str, data: list) -> None:
    """
    Write data into CSV file.

    Data is a list of lists.
    List represents lines.
    Each element (which is list itself) represents columns in a line.

    [["name", "age"], ["john", "11"], ["mary", "15"]]
    Will result in csv file:

    name,age
    john,11
    mary,15

    Use csv module here.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """
    with open(filename, 'w', newline='') as file:
        csv.writer(file).writerows(data)


def merge_dates_and_towns_into_csv(dates_file: str, towns_file: str, csv_output: str) -> None:
    """
    Merge information from two files into one CSV file.

    dates_file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    You don't have to validate the date.
    Every line contains name, colon and date.

    towns_file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_file: Input file with names and dates.
    :param towns_file: Input file with names and towns.
    :param csv_output: Output CSV-file with names, towns and dates.
    :return: None
    """
    dates = read_csv_file(dates_file, ":")
    towns = read_csv_file(towns_file, ":")

    persons = dict()
    data = ["name,town,date"]

    for date in dates:
        persons[date[0]] = [date[1] if date[1] else "-", "-"]

    for town in towns:
        if town[0] not in persons:
            persons[town[0]] = ["-", town[1] if town[1] else "-"]
        elif town[1]:
            persons[town[0]][1] = town[1]

    for name, values in persons.items():
        data.append(f"{name},{values[1]},{values[0]}")

    write_lines_to_file(csv_output, data)


def are_all_dates(dates: list) -> bool:
    """
    Check if list contains valid dates.

    :param dates: list
    :return: boolean
    """
    for date in dates:
        try:
            datetime.datetime.strptime(str(date), "%d.%m.%Y")
        except ValueError:
            if date:
                return False

    return True


def convert_to_dates(data: list) -> list:
    """
    Convert values to dates.

    :param data: list
    :return: list
    """
    return [datetime.datetime.strptime(i, "%d.%m.%Y").date() if i else None for i in data]


def try_convert_to_integers(data: list) -> list:
    """
    Convert numbers to integers if possible.

    :param data: list
    :return: list
    """
    converted = list()

    for i in data:
        if str(i).isdigit():
            converted.append(int(i))
        elif not i:
            converted.append(None)
        else:
            return data

    return converted


def read_csv_file_into_list_of_dicts(filename: str, check_datatype=False) -> list:
    """
    Read csv file into list of dictionaries.

    Header line will be used for dict keys.

    Each line after header line will result in a dict inside the result list.
    Every line contains the same number of fields.

    Example:

    name,age,sex
    John,12,M
    Mary,13,F

    Header line will be used as keys for each content line.
    The result:
    [
      {"name": "John", "age": "12", "sex": "M"},
      {"name": "Mary", "age": "13", "sex": "F"},
    ]

    If there are only header or no rows in the CSV-file,
    the result is an empty list.

    :param filename: CSV-file to read.
    :param check_datatype: bool
    :return: List of dictionaries where keys are taken from the header.
    """
    data = read_csv_file(filename)

    if len(data):
        header = data[0]
    else:
        return list()

    header_size = len(header)
    output = list()

    values = [[i[x] if i[x] != "-" and i[x] != "" else None for i in data[1:]] for x in range(header_size)] if data[1:] else list()

    if not values:
        return values

    if check_datatype:
        values = [convert_to_dates(i) if are_all_dates(i) else try_convert_to_integers(i) for i in values]

    value = 0
    for _ in range(len(data[1:])):
        dic = dict()
        for column in range(header_size):
            dic[header[column]] = values[column][value]
        value += 1
        output.append(dic)

    return output


def read_csv_file_into_list_of_dicts_using_datatypes(filename: str) -> list:
    """
    Read data from file and cast values into different datatypes.

    If a field contains only numbers, turn this into int.
    If a field contains only dates (in format dd.mm.yyyy), turn this into date.
    Otherwise the datatype is string (default by csv reader).

    Example:
    name,age
    john,11
    mary,14

    Becomes ('age' is int):
    [
      {'name': 'john', 'age': 11},
      {'name': 'mary', 'age': 14}
    ]

    But if all the fields cannot be cast to int, the field is left to string.
    Example:
    name,age
    john,11
    mary,14
    ago,unknown

    Becomes ('age' cannot be cast to int because of "ago"):
    [
      {'name': 'john', 'age': '11'},
      {'name': 'mary', 'age': '14'},
      {'name': 'ago', 'age': 'unknown'}
    ]

    Example:
    name,date
    john,01.01.2020
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': datetime.date(2020, 1, 1)},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    Example:
    name,date
    john,01.01.2020
    mary,late 2021

    Becomes:
    [
      {'name': 'john', 'date': "01.01.2020"},
      {'name': 'mary', 'date': "late 2021"},
    ]

    Value "-" indicates missing value and should be None in the result
    Example:
    name,date
    john,-
    mary,01.01.2020

    Becomes:
    [
      {'name': 'john', 'date': None},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    None value also doesn't affect the data type
    (the column will have the type based on the existing values).

    The order of the elements in the list should be the same
    as the lines in the file.

    For date, strptime can be used:
    https://docs.python.org/3/library/datetime.html#examples-of-usage-date
    """
    return read_csv_file_into_list_of_dicts(filename, True)


def write_list_of_dicts_to_csv_file(filename: str, data: list, missing="") -> None:
    """
    Write list of dicts into csv file.

    Data contains a list of dictionaries.
    Dictionary key represents the field.

    Example data:
    [
      {"name": "john", "age": "23"}
      {"name": "mary", "age": "44"}
    ]
    Will become:
    name,age
    john,23
    mary,44

    The order of fields/headers is not important.
    The order of lines is important (the same as in the list).

    Example:
    [
      {"name": "john", "age": "12"},
      {"name": "mary", "town": "London"}
    ]
    Will become:
    name,age,town
    john,12,
    mary,,London

    Fields which are not present in one line will be empty.

    The order of the lines in the file should be the same
    as the order of elements in the list.

    :param filename: File to write to.
    :param data: List of dictionaries to write to the file.
    :return: None
    """
    header = list()
    values = list()

    for content in data:
        for key in content.keys():
            if key not in header:
                header.append(key)

    if not header:
        write_csv_file(filename, list())
        return None

    for value in data:
        tmp = list()
        for i in range(len(header)):
            item = value.get(header[i])
            tmp.append(item if item is not None else missing)
        values.append(tmp)

    write_csv_file(filename, [header] + values)


def read_people_data(directory: str) -> dict:
    """
    Read people data from files.

    Files are inside directory. Read all *.csv files.

    Each file has an int field "id" which should be used to merge information.

    The result should be one dict where the key is id (int) and value is
    a dict of all the different values across the the files.
    Missing keys should be in every dictionary.
    Missing value is represented as None.

    File: a.csv
    id,name
    1,john
    2,mary
    3,john

    File: births.csv
    id,birth
    1,01.01.2001
    2,05.06.1990

    File: deaths.csv
    id,death
    2,01.02.2020
    1,-

    Becomes:
    {
        1: {"id": 1, "name": "john", "birth": datetime.date(2001, 1, 1), "death": None},
        2: {"id": 2, "name": "mary", "birth": datetime.date(1990, 6, 5), "death": datetime.date(2020, 2, 1)},
        3: {"id": 3, "name": "john", "birth": None, "death": None},
    }

    :param directory: Directory where the csv files are.
    :return: Dictionary with id as keys and data dictionaries as values.
    """
    data = list()
    keys = list()
    persons = dict()

    for file in Path(directory).glob('*.csv'):
        data.append(read_csv_file_into_list_of_dicts_using_datatypes(f"{directory}/{file.name}"))

    for file in data:
        for dic in file:
            for key in dic.keys():
                if key not in keys:
                    keys.append(key)

            for key in keys:
                person_id = dic.get("id")
                value = dic.get(key)

                if key in dic:
                    if person_id not in persons:
                        persons[person_id] = {key: value}
                    else:
                        persons[person_id][key] = value
                elif key not in persons[person_id]:
                    persons[person_id][key] = None

    return persons


def generate_people_report(person_data_directory: str, report_filename: str) -> None:
    """
    Generate report about people data.

    Data should be read using read_people_data().

    The input files contain fields "birth" and "death" which are dates. Those can be in different files. There are no duplicate headers in the files (except for the "id").

    The report is a CSV file where all the fields are written to
    (along with the headers).
    In addition, there should be two fields:
    - "status" this is either "dead" or "alive" depending on whether
    there is a death date
    - "age" - current age or the age when dying.
    The age is calculated as full years.
    Birth 01.01.1940, death 01.01.2020 - age: 80
    Birth 02.01.1940, death 01.01.2020 - age: 79

    If there is no birth date, then the age is -1.

    When calculating age, dates can be compared.

    The lines in the files should be ordered:
    - first by the age ascending (younger before older);
      if the age cannot be calculated, then those lines will come last
    - if the age is the same, then those lines should be ordered
      by birthdate descending (newer birth before older birth)
    - if both the age and birth date are the same,
      then by name ascending (a before b). If name is not available, use "" (people with missing name should be before people with name)
    - if the names are the same or name field is missing,
      order by id ascending.

    Dates in the report should in the format: dd.mm.yyyy
    (2-digit day, 2-digit month, 4-digit year).

    :param person_data_directory: Directory of input data.
    :param report_filename: Output file.
    :return: None
    """
    people = read_people_data(person_data_directory)
    output = list()

    for data in people.values():
        birth = data.get("birth")
        death = data.get("death")
        today = datetime.datetime.today().date()

        age = -1
        if birth and death:
            age = death.year - birth.year - ((death.month, death.day) < (birth.month, birth.day))
        elif birth:
            age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

        data["status"] = "dead" if death else "alive"
        data["age"] = age

        output.append(data)

    output = sorted(output, key=lambda x: (x.get('age') == -1,
                                           x.get('age'),
                                           -x.get('birth').year if x.get('birth') else "",
                                           -x.get('birth').month if x.get('birth') else "",
                                           -x.get('birth').day if x.get('birth') else "",
                                           x.get("name") if x.get("name") else "",
                                           x.get("id")))

    for data in output:
        for key in data.keys():
            value = data.get(key)
            if isinstance(value, datetime.date):
                data[key] = datetime.datetime.strftime(value, '%d.%m.%Y')

    write_list_of_dicts_to_csv_file(report_filename, output, "-")


if __name__ == '__main__':
    print(read_file_contents("read_file_contents.txt"))
    print(read_file_contents_to_list("read_file_contents_to_list.txt"))
    print(read_csv_file("read_csv_file.txt"))

    write_contents_to_file("write_contents_to_file.txt", "test 123")
    write_lines_to_file("write_lines_to_file.txt", ["test", "123"])
    write_csv_file("write_csv_file.txt", [["name", "age"], ["john", "11"], ["mary", "15"]])
    merge_dates_and_towns_into_csv("dates_file.txt", "towns_file.txt", "dates_and_towns.txt")

    print(read_csv_file_into_list_of_dicts("read_csv_file_into_list_of_dicts.txt"))
    print(read_csv_file_into_list_of_dicts_using_datatypes("read_csv_file_into_list_of_dicts_using_datatypes.txt"))

    write_list_of_dicts_to_csv_file("write_list_of_dicts_to_csv_file.txt", [{"name": "john", "age": "12"}, {"name": "mary", "town": "London"}])

    print(read_people_data("data"))
    generate_people_report("data", "generate_people_report.csv")
