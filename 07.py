import calendar


def get_today():
    day = 0
    month = 0
    year = 0
    while day == 0 or month == 0:
        try:
            day = int(input("Dzień: "))
            if day == 0 or day > 31:
                day = 0
                print("Nie ma takiego dnia miesiąca!")
                continue
            month = int(input("Miesiąc: "))
            if month == 0 or month > 12:
                month = 0
                print("Nie ma takiego miesiąca!")
                continue
            if ((month == 4 or month == 6 or month == 9 or month == 11) and day > 30) or (month == 2 and day > 29):
                print("Ten miesiąc nie ma tylu dni!")
                day = 0
                month = 0
                continue
            year = int(input("Rok: "))
            if (day == 29 and month == 2) and calendar.isleap(year) == False:
                print("Ten miesiąc nie ma tylu dni, to nie jest rok przestępny!")
                day = 0
                month = 0

        except:
            print("Niepoprwna wartość!")
    return day, month, year


def show_yesterday(today):
    this_day = today[0]
    this_month = today[1]
    this_year = today[2]

    previous_day = this_day - 1
    previous_month = this_month
    previous_year = this_year

    if previous_day == 0:
        previous_month = this_month - 1
        if previous_month == 1 or previous_month == 3 or previous_month == 5 or previous_month == 7 or previous_month == 8 or previous_month == 10 or previous_month == 12:
            previous_day = 31
        else:
            previous_day = 30
            if previous_month == 2 and calendar.isleap(this_year):
                previous_day = 29
            elif previous_month == 2 and calendar.isleap(this_year) == False:
                previous_day = 28
        if previous_month == 0:
            previous_year = this_year - 1
            previous_month = 12
            previous_day = 31
    print("Wczoraj:", previous_day, previous_month, previous_year)


def show_tommorow(today):
    this_day = today[0]
    this_month = today[1]
    this_year = today[2]

    next_day = this_day + 1
    next_month = this_month
    next_year = this_year
    if (this_month == 1 or this_month == 3 or this_month == 5 or this_month == 7 or this_month == 8 or this_month == 10 or this_month == 12) and next_day == 32:
        next_day = 1
        next_month = this_month + 1
    elif (this_month == 4 or this_month == 6 or this_month == 9 or this_month == 11) and next_day == 31:
        next_day = 1
        next_month = this_month + 1
    elif (this_month == 2 and calendar.isleap(this_year) and next_day == 30):
        next_day = 1
        next_month = this_month + 1
    elif (this_month == 2 and calendar.isleap(this_year) == False and next_day == 29):
        next_day = 1
        next_month = this_month + 1
    if next_month == 13:
        next_day = 1
        next_month = 1
        next_year = this_year + 1
    print("Jutro:", next_day, next_month, next_year)


def easter(year):
    a = year % 19
    b = int(year/100)
    c = year % 100
    d = int(b/4)
    e = b % 4
    f = int((b+8)/25)
    g = int((b-f+1)/3)
    h = (19*a+b-d-g+15) % 30
    i = int(c/4)
    k = c % 4
    l = (32+2*e+2*i-h-k) % 7
    m = int((a+11*h+22*l)/451)
    p = (h+l-7*m+114) % 31
    day = p+1
    month = int((h+l-7*m+114)/31)
    print("Wielkanoc w roku", year, "wypada -", day, month)


def day_of_the_week(today):
    this_day = today[0]
    this_month = today[1]
    this_year = today[2]
    a = (this_year - 1) % 100
    b = (this_year - 1) - a
    c = a + a / 4
    january_the_first = (((((b / 100) % 4) * 5) + c) % 7)
    if this_month == 1:
        day_of_the_year = this_day
    elif this_month == 2:
        day_of_the_year = this_day + 31
    elif this_month == 3:
        day_of_the_year = this_day + 59
    elif this_month == 4:
        day_of_the_year = this_day + 90
    elif this_month == 5:
        day_of_the_year = this_day + 12028
    elif this_month == 6:
        day_of_the_year = this_day + 151
    elif this_month == 7:
        day_of_the_year = this_day + 181
    elif this_month == 8:
        day_of_the_year = this_day + 212
    elif this_month == 9:
        day_of_the_year = this_day + 243
    elif this_month == 10:
        day_of_the_year = this_day + 273
    elif this_month == 11:
        day_of_the_year = this_day + 304
    elif this_month == 12:
        day_of_the_year = this_day + 334
    if calendar.isleap(this_year) and this_month > 2:
        day_of_the_year += 1

    days = ("Poniedziałek", "Wtorek", "Środa",
            "Czwartek", "Piątek", "Sobota", "Niedziela")
    day = (january_the_first + day_of_the_year - 1) % 7
    print("Dzisiaj:", this_day, this_month, this_year, "-", days[int(day)])


today = get_today()
show_yesterday(today)
day_of_the_week(today)
show_tommorow(today)
easter(today[2])
