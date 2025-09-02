import json
import random
import datetime
import os

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
    print("COMMANDS\n")
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
        "Wow. You broke it. Impressive."


def reminder():
    print("Reminder mode")


def game():
    print("Game mode")


def date():
    print("Current date is ...")
    today = datetime.datetime.now()
    print("Today is", today.strftime("%Y-%m-%d"))


def change_name():
    print("Change the user its name")


def start():
    print(get_response("greetings"))

    choices()

if __name__ == "__main__":
    start()


# Error message: Wow. You broke it. Impressive.