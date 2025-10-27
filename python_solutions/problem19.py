from itertools import accumulate


def divisible_by_seven(lst):
    count = 0
    for i in lst[:-1]:
        if i % 7 == 0:
            print(i)
            count += 1
    return count


def counting_sundays():
    num_sundays = 0
    sun_start_year = (
        6  # 6th January 1901 was the first sunday in our observation period
    )
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for year in range(1901, 2001):
        current_year_days = days_per_month.copy()

        if year % 4 == 0:
            current_year_days[1] += 1  # adding a day to February for leap year

        # adjust start of year to start from the first sunday
        current_year_days[0] = current_year_days[0] - sun_start_year + 1

        if (
            sun_start_year == 7
        ):  # this means the first of the year is a sunday and we need to record that
            num_sundays += 1

        # We do cumsum or accumulate on the days to get the day number of the first of the months
        # WHEN we start with the first sunday as the date of interest.
        # Basically, 7th Jan 1900 was the first sunday. so 31 days in Jan by minus 7 gives us 24.
        # So the first current_year day will correspond to how many days need to pass to get to the first of the next month (which we accomplish by adding 1)
        # So 7 (first sunday) + 25 gives us Feb 1st. In the third cumsum, gives us the day number for april 1st!
        # Then all we need to do is check for if its a sunday since aka is it diviisible by 7?

        day_num_start_of_month = list(accumulate(current_year_days))

        # print(day_num_start_of_month)

        print(day_num_start_of_month)
        num_sundays_in_year = divisible_by_seven(day_num_start_of_month)
        print(f"for year {year}, number sundays is: {num_sundays_in_year}")
        num_sundays += num_sundays_in_year

        # day_num_start_of_month[-1] -= 1

        # Now we find when the first sunday occured in the following year
        new_sunday_offset = (day_num_start_of_month[-1] - 1) % 7
        sun_start_year = 7 - new_sunday_offset

        print("======")
        print()

    return num_sundays


if __name__ == "__main__":
    print(
        "num of sundays that started on the first of the month is: ", counting_sundays()
    )
