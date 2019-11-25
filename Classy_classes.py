#this solution has been accepted by Codewars, but I have doubts whether it 
#is correct. The task itself is not clear as it is mentined that a property 
#should be created, so I have done this task twice

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = '{}s age is {}'.format(self.name, self.age)
        


#so the solution may be as follows (but I can't figure out why
#we should use a getter with public attibutes to simply print a string)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def info(self):
        return '{}s age is {}'.format(self.name, self.age)