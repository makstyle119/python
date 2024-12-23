# python

this is my journey to learn and understand python

## Folder Structure:

```
|- projects
    |- 001
        |- rock_paper_scissors_game.py
```

## Code Explaining

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
- `==` = for comparison
- `&&` = and comparison
- `||` = or comparison
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
