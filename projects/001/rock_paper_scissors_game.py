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
