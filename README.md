# python

this is my journey to learn and understand python

## Folder Structure:

```
|- lectures
    |- 001
        |- basic.py
|- projects
    |- 001
        |- rock_paper_scissors_game.py
```

## Code Explaining

- lectures/001/basic.py
    - `name = "MAK"` # this is how you define a variable in python - name and value
    - `print(name)` # this is how you print a variable
    - `type(name)` # this is how you know the type of a variable
    - `isinstance(age, int)` # this is also you can check the type of a variable - it will return true or false
    - their are various data types in `python`
        - `name = "MAK"` # string
            - string have few built in method
                - `len()` # find the length of the string
                - `.isalpha()` # check if all characters are alphabets return true or false
                - `.isalnum()` # check if all characters are digits or not empty return true or false
                - `.isdecimal()` # check if all characters are decimal return true or false
                - `.upper()` # convert text into uppercase
                - `.isupper()` # check if all characters are in uppercase return true or false
                - `.lower()` # convert text into lowercase
                - `.islower()` # check if all characters are in lowercase return true or false
                - `.title()` # convert first character of each word capital
                - `.startsswith()` # check if string start with a sub string return true or false
                - `.endswith()` # check if string end with a sub string return true or false
                - `.replace()` # replace the characters
                - `.split()` # split a string on a specific character
                - `.strip()` # to remove whitespace from a string
                - `.join()` # to append a new letter into a string
                - `.find()` # find the index of a substring
        - `age = 23` # integer
            - number have few built in method which will work all type of number (integer, decimal)
                - `abs()` # this will return absolute number (remove negative sign)
                - `round()` # convert .0-.4 to current number and .5-.9 to next number
        - `height = 5.9` # float
        - `is_student = True` # boolean
        - `hobbies = ["reading", "coding", "gaming", "sleeping"]` # list - in other languages are array
            - list have few built in method
                - `in` - `print("coding" in hobbies)` # this will return true or false and usually use in conditions
                - `[]` - `hobbies[0]`  # this will return reading - this is how you can access value of a list by index
                - `[]` - `hobbies[1:3]`  # this will return ["coding", "gaming"] - this will return data in range it will start with the first number index and end will one before last value index - and if first value is not define `hobbies[:3]` this will return data from 0 index to 2 index - and same way if last value is not provided `hobbies[1:]` this will return everything after the first index and first index is included
                - `[]` - `hobbies[1:1] = ['something_new', 'learning]` # this will add the value of the new list before the selected index -  for this your both value of the range should be same - and in will add before the current index so if we add 2 then previous value index will be 3 and on 1 and 2 our newly added value will be added
                - `insert(index, value)` # first value is the index where you want to add and second is the value which you want to add - so if you want to add fun in 1 index you will write something like this `hobbies.insert(1, "fun")`
                - `.append("some_value")` # this will add a new value in the list
                - `.extend(["some_other_value_1", "some_other_value_2"])` # this will add new list inside the existing one
                - `+= ["some_other_value_1", "some_other_value_2"]` # this will do the same thing as extend - add a new list inside the existing list
                - `.remove("sleeping")` # this will remove sleeping from the list - this way you can remove by value from a list - this course remove it from my life :-(
                - `.pop()` # this will remove last value from the list
                - `.sort()` # this will sort the list - only if data type is same of all the member of the list - it will do in ascending order - it will modified the existing list
                    - first in uppercase then in lower case
                - `len()` # find the length of the list
                - `sorted(list, way_to_sort)` # this will take first argument as list and second argument as how you want to sort the list - it will not modified the existing list
        - `address = { "city": "Karachi", "country": "Pakistan" }` # dictionary - in other language are object
            - dictionary have few built in method
                - `[key_name]` # you can write dictionary name with large bracket and inside large bracket you can provide any key name to get the value of that key - `address['city']` this will return we the name (value) of the key city which is karachi
                - `.get(key_name)` # you can also get the value of an key by using this 
                    - only benefit is with .get you can get a default value so if value doesn't get it will return a default value
                        - `address.get("region", "not provided")` # it will return not provided if region is not their
                - `.pop(key_name)` # you can delete any key from and dictionary by using this
                - `.popitem()` # it will delete last inserted item from the dictionary
                - `in` - `print("city" in address)` # this will return true or false if key is present inside the dictionary and usually use in conditions                
                - `.keys()` # it will return all the keys inside a list which is inside a dict_keys
                    - use `list(address.keys())` to get only keys
                - `.values()` # it will return all the values inside a list which is inside a dict_values
                    - use `list(address.values())` to get only values
                - `del dictionary[key_name]` # this will delete the key
                - `del dictionary.key_name` # this will also delete the key
                - `.copy()` # this will copy the entire dictionary
                - `len()` # find the length of the address
        - `complex(2, 3)` # for complex numbers
            - `print(num2.real, num2.imag)` # this is how you can print the real and imaginary part of a complex number
        - `programming_languages = ("javascript", "php", "python", "c++")` # tuples are same as list - first different we use round bracket in tuples while large bracket in list - second and most import value can't be change
            - most of the functionality is same as list
                - `in` - `print("python" in programming_languages)` # this will return true or false and usually use in conditions
                - `[]` - `programming_languages[0]`  # this will return javascript - this is how you can access value of a tuples by index
                - `.index("c++")` # this will return the index of the value - this is something we can't find in list
                - `len()` # find the length of the tuples
                - `[]` - `programming_languages[1:3]`  # this will return ["coding", "gaming"] - this will return data in range it will start with the first number index and end will one before last value index - and if first value is not define `programming_languages[:3]` this will return data from 0 index to 2 index - and same way if last value is not provided `programming_languages[1:]` this will return everything after the first index and first index is included
                - as we know you can't add anything new inside a tuples but you can combine two two make one new one `new_tuples = old_tuples1 + old_tuples2`
        - `range` # for ranges
        - `friends = {"Andomi", "Maria"}` # sets are like list - first different they use curly bracket not large - second there will be no duplicated in the set
            - one benefit sets have that they can behave like math sets so you can get
                - `&` # this will return same in both set - no duplicate
                    - `set1 = {'Moiz', 'Maria'}; set2 = {'Moiz', 'Andomi'}; common = set1 & set2; print(common) # common will only have common things in both sets - no duplicate - which is {'Moiz'}
                - `|` # this will return all the value - no duplicate
                    - `set1 = {'Moiz', 'Maria'}; set2 = {'Moiz', 'Andomi'}; all = set1 | set2; print(all) # all will have all things in both sets - no duplicate - which is {'Moiz', 'Andomi', 'Maria'}
                - `-` # this will return all the different in both sets - no duplicate
                    - `set1 = {'Moiz', 'Maria'}; set2 = {'Moiz', 'Andomi'}; sub = set1 - set2; print(sub) # sub will have only the different things from first sets - no duplicate - which is {'Maria'}
                - `<` # check if first set is sub set of second - return true or false
                    - `set1 = {'Moiz', 'Maria'}; set2 = {'Moiz', 'Andomi'}; res = set1 < set2; print(res) # return true if second set all value will be present in first set otherwise return false
                - `>` # check if second set is sub set of second - return true or false
                    - `set1 = {'Moiz', 'Maria'}; set2 = {'Moiz', 'Andomi'}; res = set1 > set2; print(res) # return true if first set all value will be present in second set otherwise return false
            - sets have few built in method
                - `len()` # find the length of the sets
    - their are 2 types of variables global variables and local variables
        - global (out of function)
        - local (inside a function)
        - in simple if something inside a function can't be use outside but outside things can be use inside the functions
    - this is how you can convert data type
        - `int("20")` # convert string to integer
        - `float(19)` # convert integer to float
        - `list(dictionary)` # convert dictionary into list - work with dictionary 
        - `list(set)` # convert set into list - work with set 
    - this is how you can concatenation
        - `print(name + " is " + str(age) + " years old.")` # this is how you concatenate a string and a variable
        - `print(f"{name} is {age} years old.")` # this is how you can also concatenate a string and a variable
    - `class State(Enum):` # this is how you create an enum in python
        - this is how you can access enum values
            - `print(State.INACTIVE.value)` # this is how you can access the enum values
            - `print(State['ACTIVE'].value)` # 1 - this is also how you can access the enum values
        - enum have few built in method
            - `list()` # this is how you can get the list of all the enum value
            - `len()` # find the length of the enum
    - you can use conditions useing if, elif and else
        - `if answer == 1:` # this is how you can use if - we write the if keyword and then the condition
        - `elif answer == 2:` # this is how you can use else if in python - we write the elif keyword and then the condition
        - `else:` # this is how you can use else in python - it will run if none of the above conditions are true
    - `input("Enter your age: ")` # this is how you can take input from the user - inside the input can be a string or empty
    `def greet(name):` # this is how you can define a function
        - we can pass function argument inside a function - inside the round bracket after function name and you have to use def before function to tell that it's a function
        - a function can be void (not returning anything) or return any data type
        - argument were use for dynamic content inside the function
        - if you update an dictionary (which is an argument inside a function) when the value will be change globally
        - to run a function you have to call it by typing function name with round bracket in the end - and if function have any parameters (function arguments call parameters) then pass then inside the round brackets - parameter can be any data types or any variable
            - `greet(name)`
        - function arguments can have default values so if function don't get any parameter we will use default value otherwise use provided value - after adding parameter you have to add is = and provide default value - default value is optional
            - `def greet(name = "user"):`
        - sometime there will be nester function - meaning function are inside a function and we call it nested functions
        - `nonlocal time` # this is how you can access a variable from the outer function - nonlocal variable - in general you can't use a variable from the outer function inside a inner function
        - closures - a closure is a function that remembers the values in enclosing scopes even if they are not present in memory (explain in code with example and code - lectures/001/basic.py:78 - lectures/001/basic.py:101)
    - `object` # everything is a object in python just like in js
        - object have few built in method (meaning you can use this with everything)
            - `.bit_length()` # return the minimum bit required for the object to keep the value
    - `loops` # we have 2 kind of loops in python
        - we have few things in both loops common
            - `continue` # this will break the current iteration and move to next
            - `break` # it will break the loop entirely
        - `while condition` # while loop will run until condition keep getting true
            - `while condition == True:` # while loop - you can use a while loop when you don't know the number of iterations
        - `for data in data_list` # for loop will run with the length of the list
            - `for hobby in hobbies:` # this is how you can use a for loop in python - you can use a for loop when you know the number of iterations
            - if you want to iterate x amount and if you know the time you can use `range(x)` to get the job done
                - `for item in range(15)` # it will give a range from 0 to 15 - (0, 15)
            - `enumerate(list)` # to get index with the value
    - `class` # a class is a blueprint for creating objects
        - `class Animal:` # this is how you can define a class - class name should be in CamelCase - just a standard
            - function inside a class is called a method
            - variables inside a class are called attributes
        - `def __init__(self, name, age, color):` # this is how you can define a constructor - a constructor is a special method that is called when an object is created - name, age and color are the attributes of the class - self is mandatory other things are optional
        - `def bark(self):` # this is how you can define a method - self is a reference to the current instance of the class
        - `class Dog (Animal):` # this is how you can inherit a class - Dog is inheriting from Animal
            - in inherit class will get everything from parent class
        - `operation overloading` # you can define the behavior of the operators
            - `def __gt__(self, other): return self.age > other.age` 
                - `print(obj1 > obj2)` # in this situation we will compare both ages or whatever we describe in the operation overloading
            - there are few more operation we can use
                - `__add__` # for +
                - `__sub__` # for -
                - `__mul__` # for *
                - `__truediv__` # for /
                - `__floordiv__` # for //
                - `__mod__` # for %
                - `__pow__` # for **
                - `__rshift__` # for >>
                - `__lshift__` # for <<
                - `__and__` # for &
                - `__or__` # for |
                - `__xor__` # for ^
    - `accepting command line arguments`
        - `name = argv[1]` # this is how you can get the command line arguments - argv is a list of command line arguments - part of sys module - argv[0] is the name of the file - argv[1] is the first argument and so on
    - `lambda num : num * 2` #  # this is how you can define a lambda function - lambda functions are anonymous functions - they are used when you need a function for a short period of time
    - `map` # return a new list - with updated values
    - `filter` # return a new list - return only the value where condition comes true
    - `reduce`# use for calculation stuff
    - `recursion` # recursion is calling function inside the function
    - `@function_name` # decorators - you can add a decorator by adding @ and then function name before the function and when you call it the decorator function will run first
    - `""" some stuff """` # add anything inside this and it will become Docstring (description)
        - `help(function_name)` # using help function you can help all the docstring related to the function
    - annotations
        - `some_other_name: string = "MAK"` # this is how you can define a variable with annotations
        - `def some_function1(name: str, age: int) -> str:` # this is how you can define a function with annotations - annotations are used to specify the type of the arguments and the return type of the function - inside function argument you can add column and then add data type you want and after round bracket ends you can add arrow -> and define return data type
    - exceptions
        - this is how you can handle exceptions - try block is used to catch exceptions - except block is used to handle exceptions - finally block is used to run the code no matter what
```
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
```

- projects/001/rock_paper_scissors_game.py
    - `import random` # this is how you import a module in python
    - `def greeting():` # def is use for function in python
    - `player_choice = 'rock'` # this is how you define a variable in python - name and value
    - `player_choice = input()` # this is how you get input from the user in python
    - `random.choice(OPTIONS)` # this is how you generate a random number in python - random.choice() - this will pick a random element from the list
    - `choices = { "player": 'rock', "computer": 'paper' }` # this is how you define a dictionary in python - dictionary is like object in js and keep key value pair - name and value
    - `print(f"Player chose: {player}")` # this is how you print a string in python - f"" - this is called f-string
    - `def check_win(player, computer):` # that's how you can add arguments to a function in python
    - `greeting()` # this is how you call a function in python - name of the function followed by ()
    - `player, computer = selected_choices.values()` # this is how you can unpack a dictionary in python
```
import random # this is how you import a module in python

OPTIONS = ["rock", "paper", "scissors"]

# def is use for function in python
def greeting():
    print("Welcome to the Rock, Paper, Scissors game!")
    print("Please choose one of the following:")
    print("rock")
    print("paper")
    print("scissors")

def get_choices():
    # this is how you define a variable in python - name and value
    # this is how you get input from the user in python
    player_choice = input()
    # this is how you generate a random number in python - random.choice() - this will pick a random element from the list
    computer_choice = random.choice(OPTIONS)

    # this is how you define a dictionary in python - dictionary is like object in js and keep key value pair - name and value
    choices = {
        "player": player_choice,
        "computer": computer_choice
    }

    return choices

def print_choices(player, computer):
    # this is how you print a string in python - f"" - this is called f-string
    print(f"Player chose: {player}")
    print(f"Computer chose: {computer}")

# that's how you can add arguments to a function in python
def check_win(player, computer):
    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer wins!")
        else:
            print("Player wins!")
    elif player == "paper":
        if computer == "scissors":
            print("Computer wins!")
        else:
            print("Player wins!")

# this is how you call a function in python - name of the function followed by ()
greeting()
selected_choices = get_choices()
# this is how you can unpack a dictionary in python
player, computer = selected_choices.values()
print_choices(player, computer)
check_win(player, computer)
```

## Logical Operators
- `+` = for addition
- `-` = for subtraction
- `*` = for multiplication
- `/` = for division
- `%` = for mod (remainder)
- `**` = for double multiplication
- `//` = for division and then round to smallest
- `==` = for comparison
- `and` = and operator
- `or` = or operator
- `in` = in operator
- `!` = not comparison
- `<` = less then comparison
- `<=` = less then and equal comparison
- `>` = greater then comparison
- `>=` = greater then and equal comparison

## Keywords
- `def` = use for function declaration
- `input` = use to get user input
- `print` = use to display data in console - just like console.log in js

## Style Guide
- `#` - this is a single line comment = use for single line comments
- Python is caseSensitive, means name and Name are two other things - `kabab case` is recommended in python, eg: my_app.
- In Python indentation is very important so don't mess with it otherwise you will be mess
