import json
import random
import datetime
import os

from format import colors
from format import text_format

MEMORY_FILE = "bot_memory.json"
RESPONSES_FILE = "bot_responses.json"


# Load memory from JSON
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)

# Save memory to JSON
def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f)


def load_responses():
    with open(RESPONSES_FILE, "r") as f:
        return json.load(f)
    

def get_response(category):
    responses = load_responses()
    if category in responses:
        return random.choice(responses[category])
    else:
        return "..."  # fallback if the category doesn’t exist
    

def Command_List():
    print(colors.YELLOW + "\nCOMMANDS\n" + colors.END)
    print("Reminder")
    print("Game")
    print("Date")
    print("Name")

    choices()

    

def choices():
    choice = input(get_response("waiting")).lower() 

    if choice == "reminder":
        reminder()
    elif choice == "game":
        game()
    elif choice == "date":
        date()
    elif choice == "name":
        change_name()
    elif choice == "commands":
        Command_List()
    elif choice == "help":
        Command_List()
    else:
        print (colors.RED + "\nWow. You broke it. Impressive." + colors.END)

        # Continue loop
        choices()


def reminder():
    print("Reminder mode")

    # Continue loop
    choices()


def game():
    print("Lets play a game, (your request not mine..)")
    print("I already have my answer")

    game_choice = input("\nRock, Paper or Scissors?").lower

    options = ["rock", "paper", "scissors"]
    if game_choice not in options:
        print("That’s not even a valid move.")
        return

    bot_choice = random.choice(options)
    print("I choose:", bot_choice)

    if game_choice == bot_choice:
        print("It’s a tie. Boring.")
    elif (
        (game_choice == "rock" and bot_choice == "scissors") or
        (game_choice == "paper" and bot_choice == "rock") or
        (game_choice == "scissors" and bot_choice == "paper")
    ):
        print("You win. Don’t get used to it.")
    else:
        print("I win. Obviously.")

    # Continue loop
    choices()


def date():
    today = datetime.datetime.now()
    print("\nToday is", today.strftime(colors.YELLOW + "%d-%m-%Y\n" + colors.END))

    # Continue loop
    choices()


def change_name():
    print("Change the user its name")

    # Continue loop
    choices()


def start():
    print(get_response("greetings"))

    # Continue loop
    choices()


if __name__ == "__main__":
    start()


# Error message: Wow. You broke it. Impressive.