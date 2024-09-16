def isLeapYear(year):
    """Checks if a given year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def daysInMonth(year, month):
    """Returns the number of days in a given month and year."""
    if month == 2:
        return 29 if isLeapYear(year) else 28
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 31


def nextDay(year, month, day):
    """Calculates the next day from a given date."""
    if day < daysInMonth(year, month):
        return year, month, day + 1
    elif month < 12:
        return year, month + 1, 1
    else:
        return year + 1, 1, 1


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Checks if one date is before another."""
    if year1 < year2:
        return True
    elif year1 == year2 and month1 < month2:
        return True
    elif year1 == year2 and month1 == month2 and day1 < day2:
        return True
    else:
        return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Calculates the number of days between two dates."""
    if dateIsBefore(year2, month2, day2, year1, month1, day1):
        raise ValueError("Second date must be after the first date.")

    days = 0
    while not dateIsBefore(year2, month2, day2, year1, month1, day1):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1

    return days


def main():
    """Main function to get user input and calculate days between dates."""
    birth_year = int(input("Enter birth year: "))
    birth_month = int(input("Enter birth month: "))
    birth_day = int(input("Enter birth day: "))

    current_year = int(input("Enter current year: "))
    current_month = int(input("Enter current month: "))
    current_day = int(input("Enter current day: "))

    days_between = daysBetweenDates(
        birth_year, birth_month, birth_day, current_year, current_month, current_day)
    print("Days between birth date and current date:", days_between)


if __name__ == "__main__":
    main()
