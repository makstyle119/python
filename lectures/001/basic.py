# imports
# this is how you import a module
from enum import Enum
from sys import argv

# variables
# this is how you define a variable - name and value
name = "MAK" # string
age = 23 # integer
float_age = float(age) # convert integer to float
height = 5.9 # float
is_student = True # boolean
hobbies = ["reading", "coding", "gaming", "sleeping"] # list - can be of any type
address = { "city": "Karachi", "country": "Pakistan" } # dictionary

# prints
# this is how you print a variable
# this is how you know the type of a variable
print(type(name)) 
# this is also you can check the type of a variable - it will return true or false
print(isinstance(age, int)) # True

# this is how you concatenate a string and a variable
print(name + " is " + str(age) + " years old.")

# this is how you can also concatenate a string and a variable
print(f"{name.lower()} is {age} years old.")

# numbers
# this is how you can get the real and imaginary part of a complex number
num1 = 2+3j
# this is also how you can get the real and imaginary part of a complex number
num2 = complex(2, 3)
# this is how you can print the real and imaginary part of a complex number
print(num2.real, num2.imag) # 2.0, 3.0

# enums
# this is how you create an enum
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

# this is how you can access the enum values
print(State.INACTIVE.value) # 0
print(State['ACTIVE'].value) # 1 - this is also how you can access the enum values
print(list(State)) # this is how you can get the list of all the enum values

# input
age = input("Enter your age: ") # this is how you can take input from the user - inside the input can be a string or empty
print(f"Your age is {age}")

# id else elif
answer = 1
# this is how you can use if - we write the if keyword and then the condition
if answer == 1:
    print("answer is 1")
# this is how you can use else if - we write the elif keyword and then the condition
elif answer == 2:
    print("answer is 2")
# this is how you can use else - it will run if none of the above conditions are true
else:
    print("answer is not 1 or 2")

# functions
# this is how you can define a function
def greet(name):
    # this is how you can define a variable inside a function - local variable
    time = 10
    # this is how you can define a function inside a function - this is a nested function
    def get_greeting_from_time():
        # this is how you can access a variable from the outer function - nonlocal variable - in general you can't use a variable from the outer function inside a inner function
        nonlocal time
        return "Good Morning" if 0 <= time else "Good Evening"
    print(f"{get_greeting_from_time()}, Hello {name}")

# this is how you can call a function
greet(name)

# closures
# this is how you can create a closure - a closure is a function that remembers the values in enclosing scopes even if they are not present in memory
def parent_function(person):
    # this is how you can define a variable inside a function - local variable
    coin = 3
    # this is how you can define a function inside a function - this is a nested function
    def coin_management():
        # this is how you can access a variable from the outer function - nonlocal variable - in general you can't use a variable from the outer function inside a inner function
        nonlocal coin
        coin -= 1
        if coin > 0:
            print(f"{person} has {coin} left")
        else:
            print(f"{person} is out of coin")
    return coin_management
    
son = parent_function("son")
daughter = parent_function("daughter")

son() # son has 2 left
son() # son has 1 left
daughter() # daughter has 2 left
son() # son is out of coin
daughter() # daughter has 1 left

# loops
# this is how you can use a for loop
condition = True
# while loop - you can use a while loop when you don't know the number of iterations
while condition == True:
    print("condition is true")
    condition = False

# this is how you can use a for loop - you can use a for loop when you know the number of iterations
for hobby in hobbies:
    print(hobby)

# Class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
# this is how you can define a class - a class is a blueprint for creating objects - class name should be in CamelCase - just a standard
# this is how you can inherit a class - Dog is inheriting from Animal
class Dog (Animal):
    # function inside a class is called a method
    #  variables inside a class are called attributes

    # this is how you can define a constructor - a constructor is a special method that is called when an object is created - name, age and color are the attributes of the class
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    # operation overloading - you can define the behavior of the operators
    def __gt__(self, other):
        return self.age > other.age

    # this is how you can define a method - self is a reference to the current instance of the class
    def bark(self):
        print("Woof")

# this is how you can create an object of a class - you have to provide the required arguments
tommy = Dog("tommy", 2, "brown") # this is how you can create an object of a class
tommy.bark() # this is how you can call a method of a class
print(tommy.name) # this is how you can access the attributes of a class

# accepting command line arguments
name = argv[1] # this is how you can get the command line arguments - argv is a list of command line arguments - part of sys module - argv[0] is the name of the file - argv[1] is the first argument and so on
print(f"Hello {name}")

# lambda functions
lambda num : num * 2 # this is how you can define a lambda function - lambda functions are anonymous functions - they are used when you need a function for a short period of time

# recursion - a function calling itself
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5)) # 120

# annotations
# this is how you can define a function with annotations - annotations are used to specify the type of the arguments and the return type of the function - inside function argument you can add column and then add data type you want and after round bracket ends you can add arrow -> and define return data type
def some_function1(name: str, age: int) -> str:
    return f"{name} is {age} years old."

some_other_name: string = "MAK" # this is how you can define a variable with annotations

# exceptions
# this is how you can handle exceptions - try block is used to catch exceptions - except block is used to handle exceptions - finally block is used to run the code no matter what
try:
    # this is how you can raise an exception
    raise Exception("This is an exception")
except Exception as e:
    print(e)
finally:
    print("This will run no matter what")
