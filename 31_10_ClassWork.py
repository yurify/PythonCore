#1.Роздрукувати всі парні числа менші 100 (написати два варіанти коду: 
# один використовуючи цикл while, а інший з використанням циклу for).

i = 0
while i<100:
    if i%2 == 0:
        print(i, end=" ")
    i = i +1

for i in range(100):
    if i%2 == 0:
        print(i, end ="")

print(list(range(0, 100, 2)))

# 2. Роздрукувати всі непарні числа менші 100. (написати два варіанти коду: 
# один використовуючи оператор continue, а інший без цього оператора).

for i in range(100):
    if i % 2 == 0:
        continue
    print (i, end=" ")


i = 0
while i < 100:
    if i % 2 == 1:
        print(i, end="")
    i = i + 1

# 3.  Перевірити чи список містить непарні числа.
#           (Підказка: використати оператор break)

spisok = [0, 4, 6, 2, 2, 3, 2, 3]
for i in spisok:
    if i % 2 == 1:
        print("There is an odd number in the list")
        break


# 4.  Створити список, який містить елементи цілочисельного типу, потім за 
# допомогою циклу перебору змінити тип даних елементів на числа з плаваючою 
# крапкою. (Підказка: використати вбудовану функцію float ()).

spisok = [0, 4, 6, 2, 2, 3, 2, 3]
for i in spisok:
    new_i = float(i)
    print(new_i, end=" ")


# 5.  Вивести числа Фібоначі включно до введеного числа n, використовуючи 
# цикли. (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)

n = int(input("How many Fibonacci numbers would you like to get? \n"))
a = 0
b = 1
print(a)
print(b)
for i in range (0, n):
    fibonacci = a + b
    print(fibonacci)
    a = b
    b = fibonacci

# 6.  Створити список, що складається з чотирьох елементів типу string. Потім, 
# за допомогою циклу for, вивести елементи по черзі на екран.

four_strings = input("Please enter 4 words: \n")
spisok = four_strings.split()
for i in spisok:
    print(i)

# 7.  Змінити попередню програму так, щоб в кінці кожної букви елементів при 
# виводі додавався певний символ, наприклад “#”. 
# (Підказка: цикл for може бути вкладений в інший цикл, а також  треба 
# використати функцію print(“ ”, end=”%”)).

four_strings = input("Please enter 4 words: \n")
spisok = four_strings.split()
for i in spisok:
    for j in i:
        print(j, end="%")
    print(" ", end="")


# 8.  Юзер вводить число з клавіатури, написати скріпт, який визначає чи 
# це число просте чи складне.

num = int(input("Введіть число більше за 1 \n"))

while num <= 1:
    num = int(input("Кхм-кхм. Потрібно ввести число більше ніж 1 \n"))

for i in range (2, num):
    if num % i == 0:  #шукаємо дільники числа num
        print(f"Число просте і найменший дільник {i}")
        break
else:
    print("Ваше число {} складне, тобто ділиться без остачі лише на 1 і на себе самого".format(num))




# 9.  Знайти максимальну цифру дійсного числа. Дійсне число 
# генеруємо випадковим чином за допомогою методу random() з модуля random
# (для цього підключаємо модуль random наступним чином 
# from random import random)

import random

while True:
    input("Click Enter to generate a number")
    num = str(random.randrange(100500))
    print("The computer has generated the following number:", num)

    for elem in range(9, -1, -1):
        if str(elem) in num:
            print("The maximum digit is", elem)
            break


# 10.  Визначити чи введене слово паліндром, тобто чи воно читається однаково
#  зліва направо і навпаки.

while True:
    st = input("Please enter a word to check ")

    i = -1
    j = 0
    
    while(i + 1 < (len(st)//2)):
        if st[i + 1] == st[j - 1]:
            print("I'm checking the letters...", st[i], "and", st[j], "are equal!")
            i = i + 1
            j = j - 1
            if (i + 1 == (len(st)//2)):
                print("This word is a palindrome!")
        else:
            print("It's not a palindrome")
            break
