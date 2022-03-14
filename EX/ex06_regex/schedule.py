"""Create schedule from the given file."""
import re
from datetime import datetime


def get_formatted_time(hours: str, minutes: str) -> str:
    """
    Format time & check if it's valid.

    :param hours: str
    :param minutes: str
    :return: string in 12-hour clock format
    """
    h = int(hours)
    m = int(minutes)

    if h >= 24 or m >= 60:
        return ""

    if h < 12:
        end = "AM"
        if h == 0:
            h = 12
    else:
        end = "PM"
        if h > 12:
            h -= 12

    return f"{h}:{m:02} {end}"


def create_sorted_schedule(input_string: str) -> list:
    """
    Create sorted schedule.

    :param input_string: str
    :return: list sorted by clock
    """
    schedule = dict()

    for match in re.finditer(r"(?<=\s|\n)(\d{1,2})\D(\d{1,2})\s+([A-Za-z]+)", input_string):
        time = get_formatted_time(match.group(1), match.group(2))
        if not time:
            continue

        item = match.group(3).lower()

        if time not in schedule:
            schedule[time] = [item]
        elif item not in schedule[time]:
            schedule[time].append(item)

    return sorted(schedule.items(), key=lambda x: datetime.strptime(x[0], '%I:%M %p'))


def create_empty_table() -> str:
    """
    Create empty table.

    Hardcoded because the size is always fixed.

    :return: empty table as string
    """
    table = ("-" * 18 + "\n")
    table += ("| {:>5} | {:<6} |".format("time", "items") + "\n")
    table += ("-" * 18 + "\n")
    table += ("| {:>3} |".format("No items found") + "\n")
    table += ("-" * 18)
    return table


def create_schedule_string(input_string: str) -> str:
    """
    Create schedule table.

    :param input_string: str
    :return: table as string
    """
    schedule = create_sorted_schedule(input_string)

    """If schedule is empty, create empty table."""
    if not schedule:
        return create_empty_table()

    max_width_time = 4  # "time" length is 4 so minimum width is always 4
    max_width_item = 5  # "items" length is 5 so minimum width is always 5

    for time, items in schedule:
        width_time = len(time)
        width_item = len(', '.join(items))

        max_width_item = width_item if max_width_item < width_item else max_width_item
        max_width_time = width_time if max_width_time < width_time else max_width_time

    max_width = max_width_time + max_width_item + 7  # 7, just magic number :)

    table = ("-" * max_width + "\n")
    table += ("| {:>{}} | {:<{}} |\n".format("time", max_width_time, "items", max_width_item))
    table += ("-" * max_width + "\n")

    for time, items in schedule:
        table += ("| {:>{}} | {:<{}} |\n".format(time, max_width_time, ', '.join(items), max_width_item))

    table += ("-" * max_width)
    return table


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    with open(input_filename) as file:
        input_string = file.read()

    table = create_schedule_string(input_string)

    with open(output_filename, "w") as file:
        file.write(table)


if __name__ == '__main__':
    print(create_schedule_string("wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
