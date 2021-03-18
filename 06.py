def get_temp():
    temp = "-"
    while temp == "-":
        try:
            temp = float(input("Podaj temperaturę: "))
        except:
            print("Niepoprawna wartość!")
    return temp

def convert_from_c(c_temp):
    fahrenheit = c_temp * 1.8 + 32
    kelvin = c_temp + 273.15
    print("temp. w F:", round(fahrenheit, 2))
    print("temp. w Kelvinach:", round(kelvin, 2))
    if fahrenheit >= 212:
        print("woda wrze")
    elif fahrenheit <= 32:
        print("woda zamarza")

def convert_from_f(f_temp):
    celsius = (f_temp - 32) / 1.8
    kelvin = celsius + 273.15
    print("temp. w C:", round(celsius, 2))
    print("temp. w Kelvinach:", round(kelvin, 2))
    if f_temp >= 212:
        print("woda wrze")
    elif f_temp <= 32:
        print("woda zamarza")

def convert_from_k(k_temp):
    celsius = k_temp - 273.15
    fahrenheit = celsius * 1.8 + 32
    print("temp. w C:", round(celsius, 2))
    print("temp. w F:", round(fahrenheit, 2))
    if fahrenheit >= 212:
        print("woda wrze")
    elif fahrenheit <= 32:
        print("woda zamarza")

def get_choice():
    print("1. Konwertuj ze stopni Celsiusza")
    print("2. Konwertuj ze stopni Fahrenheita")
    print("3. Konwertuj ze stopni Kelvina")
    choice = 0
    while choice == 0 or choice > 3:
        try:
            choice = int(input("Wybierz: "))
        except:
            print("Niepoprawna wartość!")
    return choice

choice = get_choice()
if choice == 1:
    celsius_temp = get_temp()
    convert_from_c(celsius_temp)
elif choice == 2:
    fahr_temp = get_temp()
    convert_from_f(fahr_temp)
elif choice == 3:
    kelv_temp = get_temp()
    convert_from_k(kelv_temp)