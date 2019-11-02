#3. Поміняти між собою значення двох змінних, не використовуючи третьої змінної.

a = input("Please enter variable a: ")
b = input("Please enter variable b: ")
print("a is {}, b is {}".format(a, b))
a, b = b, a
print("Let's reverse the variables:\na is {}, b is {}".format(a, b))