# # 1.  Написати функцію, яка знаходить середнє арифметичне значення довільної 
# # кількості чисел. 
# # 2.  Написати функцію, яка повертає абсолютне значення числа
# # 3.  Написати функцію, яка знаходить максимальне число з двох чисел, 
# # а також в функції використати рядки документації DocStrings.


# #1
# def average(*args):
#     "This function will return the average of your parameters"
#     sum = 0
#     for num in args:
#         sum = sum + num
#         avg = sum/len(args)
#     return avg

# def avg1(*args):
#     return sum(args)/len(args)

# print(average(5, 10, 15))
# print(avg1(5, 10, 15))
# # 2.  Написати функцію, яка повертає абсолютне значення числа

# def absolute(num):
#     "Returns the absolute value of the number"
#     return abs(num)

# def absolute1(num):
#     "Returns the absolute value of the number"
#     if num == 0:
#         return 0
#     elif num > 0:
#         return num
#     else:
#         return num * (-1)

# def absolute2(num):
#     if num >= 0:
#         return num
#     else:
#         return -num

# print(absolute(-56))

# print(absolute1(-56))


# 3.  Написати функцію, яка знаходить максимальне число з двох чисел, 
# а також в функції використати рядки документації DocStrings.

# def maximum(num1, num2):
#     """This function
#     returns maximum
#     """
#     if num1 > num2:
#         return ("The maximum number is", num1)
#     elif num1 < num2:
#         return ("The maximum number is", num2)
#     else:
#         return "The numbers are equal"

# print(maximum(25, 35))


#4

def rectange_square():
    "This function calculates the square of a rectangle"
    a = int(input("Please enter the lenght:"))
    b = int(input("Please enter the width:"))
    return print("The square is", a * b)    
     

def triangle_square():
    "This function calculates the square of a triangle"
    a = int(input("Please enter a:"))
    h = int(input("Please enter height:"))
    return print("The square is", 0.5*a*h)

def circle_square():
    "This function calculates the square of a circle"
    r = int(input("Please enter the radius:"))
    return print("The square is", 3.14*r*r)
    

shape = input("Please select the shape: \n1. Rectangle \n2. Triange \n3. Circle\n")

if shape == '1':
    rectange_square()
elif shape == '2':
    triangle_square()
elif shape == '3':
    circle_square()
else:
    print("Please enter either 1, 2 or 3 :)")