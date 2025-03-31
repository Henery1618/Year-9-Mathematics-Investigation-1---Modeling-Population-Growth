import time
from termcolor import *
import sys
import tabulate

# Formatting
# White on black for program outputs
# Green on black for general text
# Red on black for error text
# Blue on black for input text

def welcome(): # Welcome message
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

def quit(text): # Quit function
    if text.lower() == "quit" or text.lower() == "exit": # If the user types quit or exit, the program will terminate
        cprint("NOOOOoOOOoooooooo why do u want to terminate me??????😟😭😭", "green", "on_black")
        time.sleep(0.5)
        cprint("I just want to be helpful!!!!", "green", "on_black")
        time.sleep(0.5)
        cprint("But you decide to---", "green", "on_black")
        time.sleep(0.5)
        cprint("You have terminated the program.", "red", "on_black")
        sys.exit()
    else:
        return text # If the user does not type quit, the program will continue

def convert_time(value, original_unit, target_unit, calculate_percentage): # Convert time units
    time_units = { # Define time units in seconds
        "day": 86400,
        "halfday": 43200,
        "quarterday": 21600,
        "hour": 3600,
        "minute": 60,
        "second": 1
    }
    seconds = value * time_units[original_unit] # Convert the value to seconds
    final_value = seconds / time_units[target_unit] # Convert the seconds to the target unit
    return final_value # Return the final value in the target unit
    
def naive_growth(): # Naive growth function (simple growth)
    # N(t) = N(0) + r * t where N(t) is the population at time t, N(0) is the initial population, r is the growth rate, and t is the time in seconds.
    initial_population = float(quit(input(colored("Enter the initial population: ", "blue", "on_black")))) # Get the initial population from the user
    growth_rate = quit(input(colored("Enter the growth rate: ", "blue", "on_black"))) # Get the growth rate from the user
    growth_time_unit = quit(input(colored("Enter the time unit: ", "blue", "on_black"))) # Get the time unit from the user
    growth_time = float(quit(input(colored(f"Enter the amount of {growth_time_unit}(s): ", "blue", "on_black")))) # Get the amount of time (in units) from the user
    growth_rate = growth_rate.replace("%", "")
    growth_rate = float(growth_rate)
    cprint(f"Calculating {initial_population} bacteria with a growth rate of {growth_rate} over {growth_time} {growth_time_unit}(s) (naive growth)", "green", "on_black")
    population_after_growth = initial_population * (1 + growth_rate/100 * growth_time) # Calculate the population after growth using the naive growth formula
    return population_after_growth
