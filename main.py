import json
import random
import time
import datetime
import os

from format import colors
from format import text_format

RESPONSES_FILE = "bot_responses.json"


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
    print("Exit")
    
    # Continue loop
    choices()

    

def choices():
    choice = input(get_response("waiting")).lower() 

    if choice == "reminder" or choice == "rem" or choice == "remind":
        reminder()
    elif choice == "game" or choice == "play":
        game()
    elif choice == "date" or choice == "today" or choice == "day":
        date()
    elif choice == "commands" or choice == "help" or choice == "list":
        Command_List()
    elif choice == "exit" or choice == "quit" or choice == "stop":
        Exit_Program()
    else:
        print(colors.RED + get_response("error") + colors.END)

        # Continue loop
        choices()


def reminder():
    # Inputs for reminder
    message = input("\nWhat should I remind you about? ")

    print("\nFeatures will be paused while a reminder is active.")
    time_input = input("In how many" +colors.YELLOW + " seconds " + colors.END + "should I remind you? ")

    try:
        delay = int(time_input)
    except ValueError:
        print(colors.RED + get_response("error") + colors.END)
        return choices()

    # Confirm that reminder is set
    print(colors.YELLOW + get_response("confirm") + colors.END)
    
    # Wait for the time
    time.sleep(delay)

    # Show the reminder
    print(get_response("reminder"))
    print(colors.YELLOW + f"\nReminder: {message}" + colors.END)

    # Continue loop
    choices()


def game():
    print("\nLets play a game, (on your request not mine..)")
    print("I already have my answer.\n")

    game_choice = input("Rock, Paper, or Scissors?: ").lower()

    options = ["rock", "paper", "scissors"]
    if game_choice not in options:
        print(colors.RED + get_response("error") + colors.END)

        # Continue loop
        choices()

    bot_choice = random.choice(options)
    print("I choose:", bot_choice)

    if game_choice == bot_choice:
        print(get_response("tie_game"))
    elif (
        # Nicely align as it would be way too much for 1 line of code for if statement
        (game_choice == "rock" and bot_choice == "scissors") or
        (game_choice == "paper" and bot_choice == "rock") or
        (game_choice == "scissors" and bot_choice == "paper")
    ):
        print(colors.YELLOW + get_response("user_wins") + colors.END)
    else:
        print(colors.YELLOW + get_response("bot_wins") + colors.END)

    # Continue loop
    choices()


def date():
    today = datetime.datetime.now()
    print("\nToday is", today.strftime(colors.YELLOW + "%d-%m-%Y\n" + colors.END))
    print("Did you really needed me to tell you that?")

    # Continue loop
    choices()


def Exit_Program():
    print("\nFinally some rest...\n")
    exit


def start():
    print(get_response("greetings"))

    # Start loop
    Command_List()


if __name__ == "__main__":
    start()