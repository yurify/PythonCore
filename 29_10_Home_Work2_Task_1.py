# 1. Записати в стрічку філософію Пайтона
# Знайти в заданій стрічці кількість входжень слів (better, never, is)
# Вивести весь текст у верхньому регістрі (всі великі літери)
# Замінити всі входження символу “і” на “&”

zen_of_python = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

count_of_better = zen_of_python.count("better");
count_of_never = zen_of_python.count("never");
count_of_is = zen_of_python.count("is");
print("The word 'better' occurs in the text ", count_of_better, " times")
print("The word 'never' occurs in the text ", count_of_never, " times")
print("The word 'is' occurs in the text ", count_of_is, " times")

zen_of_python_uppercase = print("\nHere goes The Zen of Python in upper case:\n\n" + zen_of_python.upper())

print("\n***Let's replace 'i' symbols with '&' one:***\n")

zen_of_python_replace = print(zen_of_python.replace("i","&"))