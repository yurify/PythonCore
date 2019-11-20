# import pyowm

# owm = pyowm.OWM('04c112a884dfb41e282cf5a0898a5259')  # You MUST provide a valid API key

# city = input("Please enter the city: ")

# # Search for current weather in London (Great Britain)
# observation = owm.weather_at_place(city)
# w = observation.get_weather()
# #print(w)                      # <Weather - reference time=2013-12-18 09:20,
#                               # status=Clouds>

# # Weather details
# wind = w.get_wind()                  # {'speed': 4.6, 'deg': 330}
# humid = w.get_humidity()              # 87
# temp = w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# # Search current weather observations in the surroundings of
# # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# observation_list = owm.weather_around_coords(-22.57, -43.12)

# print(f"In city {city} wind speed is {wind['speed']}, temperature is {temp['temp']}")






#1.  Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисел від 1 до 100 і пропонує 
# користувачу вгадати це число. Програма зчитує числа, які вводить користувач і видає користувачу підказки 
# про те чи загадане число більше чи менше за введене користувачем. Гра має тривати до моменту поки користувач 
# не введе число, яке загадане програмою, тоді друкує повідомлення привітання. 
#(для виконання завдання необхідно імпортувати  модуль random, а з нього функцію randint())

import random
num = random.randint(1, 100)
print("The computer has generated:", num)





while True:
    guess = int(input("Please enter the number:"))
    if guess == num:
        print("You guessed!")
        break 
    elif num>guess:
        print("choose a bigger number")
    elif num<guess:
        print("choose a smaller number")    




# 2. Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2. 
# (для виконання завдання необхідно імпортувати  модуль math, а з нього функцію pow() та значення змінної пі).



