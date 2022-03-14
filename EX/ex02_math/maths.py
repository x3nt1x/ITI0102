"""Math."""


def ects(ects, weeks):
    """
    Implement a function to know how many hours are needed per week if each ECTS is 26 hours. If it's not possible in time then return a string "Impossible!".

    Examples:
    1. ects(30, 12) == 65
    2. ects(1, 1) == 26
    3. ects(1, 0) == "Impossible!"
    """
    if weeks > 0:
        return (ects * 26) / weeks
    else:
        return "Impossible!"


def average(a, b, c, d):
    """
    Implement a function that has 4 numeric parameters. Each parameter must be multiplied by number of its position in the function (x, y, z = 1, 2, 3). Calculate and return the average.

    Examples:
    1. average(0, 0, 0, 4) === 4
    2. average(1, 2, 3, 4) == 7.5
    3. average(5, 0, 5, 1) == 6
    """
    b *= 2
    c *= 3
    d *= 4

    return ((a + b + c + d) / 4)


def clock(days, hours, minutes, seconds):
    """
    Implement a function that has 4 numeric parameters. The values are: days, hours, minutes, seconds. Calculate how many minutes are in total and return the value.

    Examples:
    1. clock(1, 24, 60, 60) === 2941
    3. clock(0, 0, 0, 60) == 1
    3. clock(0, 0, 1, 60) == 2
    """
    days *= 1440  # Convert days to minutes
    hours *= 60  # Convert hours to minutes
    seconds /= 60  # Convert seconds to minutes

    return (days + hours + minutes + seconds)


if __name__ == '__main__':
    print(ects(30, 12))
    print(ects(1, 1))
    print(ects(1, 0))

    print(average(0, 0, 0, 4))
    print(average(1, 2, 3, 4))
    print(average(5, 0, 5, 1))

    print(clock(1, 24, 60, 60))
    print(clock(0, 0, 0, 60))
    print(clock(0, 0, 1, 60))
