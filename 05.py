def choose_currency():
    currencies = ["USD", "THB", "BTC", "BTN", "MRO", "ETH"]
    print("1.", currencies[0], "<--->", currencies[1])
    print("2.", currencies[0], "<--->", currencies[2])
    print("3.", currencies[0], "<--->", currencies[3])
    print("4.", currencies[0], "<--->", currencies[4])
    print("5.", currencies[0], "<--->", currencies[5])
    choice = input("Wybierz: ")
    while choice.isdigit() == False or len(choice) != 1 or int(choice) == 0 or int(choice) > len(currencies)-1:
        choice = input("Wybierz jedną cyfrę: ")
    print("1.", currencies[0], "-->", currencies[int(choice)])
    print("2.", currencies[int(choice)], "-->", currencies[0])
    direction_choice = input("Wybierz: ")
    while direction_choice.isdigit() == False or len(direction_choice) != 1 or int(direction_choice) == 0 or int(direction_choice) > 2:
        direction_choice = input("Wybierz jedną cyfrę: ")
    chosen_currency = currencies[int(choice)]
    if int(direction_choice) == 1:
        curr_from = currencies[0]
        curr_to = chosen_currency
    elif int(direction_choice) == 2:
        curr_from = chosen_currency
        curr_to = currencies[0]
    value = -1
    while float(value) < 0:
        try:
            value = float(input("Podaj wartość w " + curr_from + ": "))
        except:
            print("Niepoprawna wartość!")
    return currencies, curr_from, curr_to, value

def calculate(choices):
    currencies = choices[0]
    curr_from = choices[1]
    curr_to = choices[2]
    value = choices[3]
    if curr_from == currencies[0]:
        if curr_to == currencies[1]:
            result = value * 30.7
        elif curr_to == currencies[2]:
            result = value * 0.000017
        elif curr_to == currencies[3]:
            result = value * 72.67
        elif curr_to == currencies[4]:
            result = value * 35.96
        elif curr_to == currencies[5]:
            result = value * 0.00053
    elif curr_from == currencies[1]:
        result = value * 0.033
    elif curr_from == currencies[2]:
        result = value * 59909.3
    elif curr_from == currencies[3]:
        result = value * 0.014
    elif curr_from == currencies[4]:
        result = value * 0.028
    elif curr_from == currencies[5]:
        result = value * 1885
    return value, result, curr_from, curr_to

def show_results(results):
    print(round(results[0],2), results[2], "=", round(results[1], 2), results[3])

user_choices = choose_currency()
calc_results = calculate(user_choices)
show_results(calc_results)