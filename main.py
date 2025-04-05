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
change_menu_bool = False

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
    global menu_num, repeat_menu, change_menu_bool
    print()
    cprint("Please select an option:", "green", "on_black")
    cprint("1. Naive Growth (simple growth)", "green", "on_black")
    cprint("2. Sophisticated Growth (exponential growth)", "green", "on_black")
    cprint("3. Naive vs Sophisticated growth comparison", "green", "on_black")
    cprint("4. Projected time until a certain population is reached (exponential growth)", "green", "on_black")
    cprint("5. Comparing sophisticated growth with different growth rates", "green", "on_black")
    menu_num = quit(input(colored("Enter your choice: ", "blue", "on_black"))) # Get the user's choice
    while not menu_num.isnumeric() or int(menu_num) < 1 or int(menu_num) > 5:
        cprint("Please enter a valid choice.", "red", "on_black")
        menu_num = quit(input(colored("Enter your choice: ", "blue", "on_black"))) # Get the user's choice
    repeat_menu = quit(input(colored("Do you want to loop the selected menu?: ", "blue", "on_black")))
    while repeat_menu.lower() not in true_inputs and repeat_menu.lower() not in false_inputs:
        cprint("Please enter a valid choice.", "red", "on_black")
        repeat_menu = quit(input(colored("Do you want to loop the selected menu?: ", "blue", "on_black")))
    menu_num = int(menu_num) # Convert the menu number to an integer
    change_menu_bool = False

def change_menu(text):
    global change_menu_bool
    if text.lower() == "menu":
        change_menu_bool = True
    else:
        return text

def convert_time(value, original_unit, target_unit, calculate_percentage): # Convert time units
    if not calculate_percentage:
        final_value = value * time_units[original_unit] / time_units[target_unit] # Convert the value to seconds and then to the target unit
    else:
        final_value = (value / time_units[original_unit]) * time_units[target_unit] * 100 # Adjusted percentage calculation
    return final_value # Return the final value in the target unit

def is_float(value): # Check if the value is a float
    if value == None:
        return False # If the value is None, return False
    try:
        float(value) # Try to convert the value to a float
        return float(value)
    except ValueError:
        cprint("Please enter a valid number.", "red", "on_black")
        return False # If unsuccessful, return False

def is_percentage(value): # Check if the value is a percentage
    if value == None:
        return False # If the value is None, return False
    value = value.replace("%", "") # Remove the % sign from the value
    if is_float(value) == False: # If the value is not a number, return False
        cprint("Please enter a valid percentage.", "red", "on_black")
        return False
    return float(value)/100 # Return the value as a decimal

def input_time_error_check(input_time):
    if input_time == None:
        return False # If the input is None, return False
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

def growth_inputs():
    if change_menu_bool == False:
        initial_population = is_float(change_menu(quit(input(colored("Enter the initial population: ", "blue", "on_black"))))) # Get the initial population from the user
        while initial_population == False and change_menu_bool == False: # If the input is not a number, ask for the input again
            initial_population = is_float(change_menu(quit(input(colored("Enter the initial population: ", "blue", "on_black"))))) # Ask for the input again
    if change_menu_bool == False:
        growth_rate = is_percentage(change_menu(quit(input(colored("Enter the growth rate: ", "blue", "on_black"))))) # Above comments apply to the other inputs as well
        while growth_rate == False and change_menu_bool == False:
            growth_rate = is_percentage(change_menu(quit(input(colored("Enter the growth rate: ", "blue", "on_black")))))
    if change_menu_bool == False:
        growth_time_period = input_time_error_check(change_menu(quit(input(colored(f"Enter the time for one growth period: ", "blue", "on_black")))))
        while growth_time_period == False and change_menu_bool == False:
            growth_time_period = input_time_error_check(change_menu(quit(input(colored(f"Enter the time for one growth period: ", "blue", "on_black")))))
    if change_menu_bool == False:
        growth_time = input_time_error_check(change_menu(quit(input(colored("Enter the amount of time to project into the future: ", "blue", "on_black")))))
        while growth_time == False and change_menu_bool == False:
            growth_time = input_time_error_check(change_menu(quit(input(colored("Enter the amount of time to project into the future: ", "blue", "on_black")))))
    if change_menu_bool == False:
        return [initial_population, growth_rate, growth_time_period, growth_time] # Return the inputs as a list

def naive_growth(is_comparison): # Naive growth function (simple growth)
    global change_menu_bool
    # N(t) = N(0) + (N(0) * r * t) where N(t) is the population at time t, N(0) is the initial population, r is the growth rate, and t is the time
    if not is_comparison:
        cprint("\nNaive Growth (simple growth) Calculator!", "green", "on_black")
        inputs = growth_inputs() # Get the inputs from the user
    else:
        inputs = is_comparison
    # Calculate the simple growth
    if change_menu_bool == False:
        cprint(f"Calculating naive (simple) growth of {inputs[0]} with a growth rate of {inputs[1]*100}% every {inputs[2][0]} {inputs[2][1]}(s), over a period of {inputs[3][0]} {inputs[3][1]}(s)...", "green", "on_black")
        total_time_periods = convert_time(inputs[3][0], inputs[3][1], inputs[2][1], False) / inputs[2][0] # Calculate how many growth periods are in the total time
        final_amount = inputs[0] + (inputs[0] * inputs[1] * total_time_periods) # Calculate the final amount using the formula N(t) = N(0) + (N(0) * r * t)
        return [inputs[0], inputs[1], inputs[2], inputs[3], final_amount] # Return the final amount

def sophisticated_growth(is_comparison): # Sophisticated growth function (exponential growth)
    global change_menu_bool
    # N(t) = N(0) * (1 + r)^t where N(t) is the population at time t, N(0) is the initial population, r is the growth rate, and t is the time
    if not is_comparison:
        cprint("\nSophisticated Growth (exponential growth) Calculator!", "green", "on_black")
        inputs = growth_inputs() # Get the inputs from the user
    else:
        inputs = is_comparison
    # Calculate the exponential growth
    if change_menu_bool == False:
        cprint(f"Calculating sophisticated (exponential) growth of {inputs[0]} with a growth rate of {inputs[1]*100}% every {inputs[2][0]} {inputs[2][1]}(s), over a period of {inputs[3][0]} {inputs[3][1]}(s)...", "green", "on_black")
        total_time_periods = convert_time(inputs[3][0], inputs[3][1], inputs[2][1], False) / inputs[2][0] # Calculate how many growth periods are in the total time
        final_amount = inputs[0] * (1 + inputs[1])**total_time_periods
        return [inputs[0], inputs[1], inputs[2], inputs[3], final_amount]

def compare_growth():
    global change_menu_bool
    # Compare naive and sophisticated growth
    cprint("\nNaive vs Sophisticated Growth Comparison!", "green", "on_black")
    inputs = growth_inputs() # Get the inputs from the user
    naive_result = naive_growth(inputs) # Get the result from the naive growth function
    sophisticated_result = sophisticated_growth(inputs) # Get the result from the sophisticated growth function
    if change_menu_bool == False:
        cprint(f"Comparing naive and sophisticated growth of {inputs[0]} with a growth rate of {inputs[1]*100}% every {inputs[2][0]} {inputs[2][1]}(s), over a period of {inputs[3][0]} {inputs[3][1]}(s)...", "green", "on_black")
        return [["Naive Growth", naive_result[4]], ["Sophisticated Growth", sophisticated_result[4]]] # Create a table to display the results

welcome()
while True:
    menu()
    while menu_num == 1:
        result = naive_growth(False)
        if change_menu_bool == False:
            print()
            cprint(f"Starting with an initial population of {result[0]}, growing simply at a rate of {result[1]*100}% every {result[2][0]} {result[2][1]}(s), over a total time of {result[3][0]} {result[3][1]}(s), the final population is projected to be {result[4]:.2f} bacteria.", "green", "on_black")
        if repeat_menu in false_inputs or change_menu_bool == True:
            break
    while menu_num == 2:
        result = sophisticated_growth(False)
        if change_menu_bool == False:
            print()
            cprint(f"Starting with an initial population of {result[0]}, growing exponentially at a rate of {result[1]*100}% every {result[2][0]} {result[2][1]}(s), over a total time of {result[3][0]} {result[3][1]}(s), the final population is projected to be {result[4]:.2f} bacteria.", "green", "on_black")
        if repeat_menu in false_inputs or change_menu_bool == True:
            break
    while menu_num == 3:
        result = compare_growth()
        if change_menu_bool == False:
            print()
            cprint(tabulate.tabulate(result, headers=["Growth Type", "Final Population"]), "green", "on_black")
        if repeat_menu in false_inputs or change_menu_bool == True:
            break