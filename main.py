import time
from termcolor import *
import sys
import tabulate

# Formatting
# White on black for program outputs
# Green on black for general text
# Red on black for error text
# Blue on black for input text

def welcome():
    cprint(f" _    _        _", "white", "on_black")
    time.sleep(0.1)
    cprint(f"| |  | |      | |", "white", "on_black")
    time.sleep(0.1)
    cprint(f"| |  | |  ___ | |  ___   ___   _ __ ___    ___", "white", "on_black")
    time.sleep(0.1)
    cprint(f"| |/\| | / _ \| | / __| / _ \ | '_ ` _ \  / _ \'", "white", "on_black")
    time.sleep(0.1)
    cprint(f"\  /\  /|  __/| || (__ | (_) || | | | | ||  __/", "white", "on_black")
    time.sleep(0.1)
    cprint(f" \/  \/  \___||_| \___| \___/ |_| |_| |_| \___|", "white", "on_black")
    time.sleep(0.25)
    cprint("Welcome to my Mathematics Investigation!", "green", "on_black")
    time.sleep(0.25)
    cprint("If you decide to quit the program at any point, type quit! (Your results will automatically display)", "green", "on_black")
    print()

def quit(text):
    if text.lower() == "quit":
        cprint("NOOOOoOOOoooooooo why do u want to terminate me??????😟😭😭", "green", "on_black")
        time.sleep(0.5)
        cprint("I just want to be helpful!!!!", "green", "on_black")
        time.sleep(0.5)
        cprint("But you decide to---", "green", "on_black")
        time.sleep(0.5)
        cprint("You have terminated the program.", "red", "on_black")
        sys.exit()
    else:
        return text

def convert_time(value, original_unit, target_unit):
    time_units = {
        "day": 86400,
        "halfday": 43200,
        "quarterday": 21600,
        "hour": 3600,
        "minute": 60,
        "second": 1
    }
    seconds = value * time_units[original_unit]
    final_value = seconds / time_units[target_unit]
    return final_value