import time
from termcolor import *
import sys
import tabulate

# Formatting
# Green on black for general text
# Red on black for error text
# Blue on black for input text

time_units = { # Define time units in seconds
    "day": 86400,
    "halfday": 43200,
    "quarterday": 21600,
    "hour": 3600,
    "minute": 60,
    "second": 1
}
true_inputs = ["yes", "y", "true", "t", "1"] # Define true inputs for yes/no questions
false_inputs = ["no", "n", "false", "f", "0"] # Define false inputs for yes/no questions

menu_num = "Null"
repeat_menu = "Null"

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
    cprint("If you decide to quit the program at any point, type quit!", "green", "on_black")
    time.sleep(0.25)
    cprint("If you want to view the menu again, type menu!", "green", "on_black")

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

def menu():
    global menu_num, repeat_menu
    print()
    cprint("Please select an option:", "green", "on_black")
    cprint("1. Naive Growth (simple growth)", "green", "on_black")
    cprint("2. Sophisticated Growth (exponential growth)", "green", "on_black")
    cprint("3. Naive vs Sophisticated growth comparison", "green", "on_black")
    cprint("4. Projected time until a certain population is reached (exponential growth)", "green", "on_black")
    cprint("5. Comparing sophisticated growth with different growth rates", "green", "on_black")
    menu_num = input(colored("Enter your choice: ", "blue", "on_black")) # Get the user's choice
    while not menu_num.isnumeric() or int(menu_num) < 1 or int(menu_num) > 5:
        cprint("Please enter a valid choice.", "red", "on_black")
        menu_num = input(colored("Enter your choice: ", "blue", "on_black")) # Get the user's choice
    repeat_menu = input(colored("Do you want to loop the selected menu?: ", "blue", "on_black"))
    while repeat_menu.lower() not in true_inputs and repeat_menu.lower() not in false_inputs:
        cprint("Please enter a valid choice.", "red", "on_black")
        repeat_menu = input(colored("Do you want to loop the selected menu?: ", "blue", "on_black"))
    menu_num = int(menu_num) # Convert the menu number to an integer

def convert_time(value, original_unit, target_unit, calculate_percentage): # Convert time units
    if not calculate_percentage:
        final_value = value * time_units[original_unit] / time_units[target_unit] # Convert the value to seconds and then to the target unit
    else:
        final_value = (value / time_units[original_unit]) * time_units[target_unit] * 100 # Adjusted percentage calculation
    return final_value # Return the final value in the target unit

def is_float(value): # Check if the value is a float
    try:
        float(value) # Try to convert the value to a float
        return float(value)
    except ValueError:
        cprint("Please enter a valid number.", "red", "on_black")
        return False # If unsuccessful, return False

def is_percentage(value): # Check if the value is a percentage
    value = value.replace("%", "") # Remove the % sign from the value
    if is_float(value) == False: # If the value is not a number, return False
        cprint("Please enter a valid percentage.", "red", "on_black")
        return False
    return float(value)/100 # Return the value as a decimal

def input_time_error_check(input_time):
    input_time = input_time.lower()
    while "f d" in input_time or "r d" in input_time: # Remove the space between time with days on the end
        input_time = input_time.replace(" d", "d")
    while "  " in input_time: # Remove extra spaces
        input_time = input_time.replace("  ", " ")
    input_time = input_time.split(" ")
    while input_time[1].endswith("s"): # Remove trailing "s"
        input_time[1] = input_time[1][:-1]
    if not is_float(input_time[0]) or input_time[1] not in time_units or len(input_time) != 2: # Validate input
        cprint("Please enter a valid time.", "red", "on_black")
        return False
    input_time[0] = float(input_time[0]) # Convert the first element to a float
    return input_time

def naive_growth(): # Naive growth function (simple growth)
    # N(t) = N(0) + (N(0) * r * t) where N(t) is the population at time t, N(0) is the initial population, r is the growth rate, and t is the time in seconds.
    cprint("\nNaive Growth (simple growth) Calculator!", "green", "on_black")
    initial_population = is_float(quit(input(colored("Enter the initial population: ", "blue", "on_black")))) # Get the initial population from the user
    while initial_population == False: # If the input is not a number, ask for the input again
        initial_population = is_float(quit(input(colored("Enter the initial population: ", "blue", "on_black")))) # Ask for the input again
    growth_rate = is_percentage(quit(input(colored("Enter the growth rate: ", "blue", "on_black")))) # Above comments apply to the other inputs as well
    while growth_rate == False:
        growth_rate = is_percentage(quit(input(colored("Enter the growth rate: ", "blue", "on_black"))))
    growth_time_period = input_time_error_check(quit(input(colored(f"Enter the time for one growth period: ", "blue", "on_black"))))
    while growth_time_period == False:
        growth_time_period = input_time_error_check(quit(input(colored(f"Enter the time for one growth period: ", "blue", "on_black"))))
    growth_time = input_time_error_check(quit(input(colored("Enter the amount of time to project into the future: ", "blue", "on_black"))))
    while growth_time == False:
        growth_time = input_time_error_check(quit(input(colored("Enter the amount of time to project into the future: ", "blue", "on_black"))))
    # Calculate the simple interest
    cprint(f"Calculating growth of {initial_population} with a growth rate of {growth_rate*100}% over a period of {growth_time[0]} {growth_time[1]}(s) with a growth period of {growth_time_period[0]} {growth_time_period[1]}(s)...", "green", "on_black")
    total_time_periods = convert_time(growth_time[0], growth_time[1], growth_time_period[1], False) / growth_time_period[0] # Calculate how many growth periods are in the total time
    final_amount = initial_population + (initial_population * growth_rate * total_time_periods) # Calculate the final amount using the formula N(t) = N(0) + (N(0) * r * t)
    return final_amount # Return the final amount

welcome()
while True:
    menu()
    while menu_num == 1:
        print(naive_growth())
        if repeat_menu in true_inputs:
            continue
        else:
            break