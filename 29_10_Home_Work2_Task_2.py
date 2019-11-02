# 2. Задано чотирицифрове натуральне число.
# Знайти добуток цифр цього числа.
# Записати число в реверсному порядку.
# Посортувати цифри, що входять в дане число

#Добуток цифр
user_number = input("Please enter a 4-digit number:\n   ")
multiple = int(user_number[0])*int(user_number[1])*int(user_number[2])*int(user_number[3])
print ("The multiple is: ", multiple)

# Записати число в реверсному порядку.
reverse = user_number[3] + user_number[2] + user_number[1] + user_number[0]
print ("Reverse number is: ", reverse)

# Посортувати цифри, що входять в дане число
print (sorted(user_number))