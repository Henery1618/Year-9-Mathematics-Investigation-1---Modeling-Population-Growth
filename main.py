import time
from termcolor import *
import sys
import tabulate
import math

# Formatting
# Green on black for general text
# Red on black for error text
# Blue on black for input text

time_units = { # Define time units in seconds
    "year": 31104000,
    "quarter": 7776000,
    "month": 2592000,
    "week": 604800,
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

millnames = ["",
             " Thousand",
             " Million",
             " Billion",
             " Trillion",
             " Quadrillion",
             " Quintillion",
             " Sextillion",
             " Septillion",
             " Octillion",
             " Nonillion",
             " Decillion",
             " Undecillion",
             " Duodecillion",
             " Tredecillion",
             " Quattuordecillion",
             " Quindecillion",
             " Sexdecillion",
             " Septendecillion",
             " Octodecillion",
             " Novemdecillion",
             " Vigintillion",
             " Unvigintillion",
             " Duovigintillion",
             " Trevigintillion",
             " Quattuorvigintillion",
             " Quinvigintillion",
             " Sexvigintillion",
             " Septenvigintillion",
             " Octovigintillion",
             " Novemvigintillion",
             " Trigintillion",
             " Untrigintillion",
             " Duotrigintillion"
             ]
# Adds the large numbers and rounds to one decimal
def millify(n):
    n = float(n)
    millidx = max(0, min(len(millnames) - 1, int(math.floor(0 if n == 0 else math.log10(abs(n)) / 3))))
    return '{:.1f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

def no_millify(n):
    return n

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
    cprint("3. Naive vs Sophisticated growth comparison (p1)", "green", "on_black")
    cprint("4. Projected time until a certain population is reached (exponential growth) (p2)", "green", "on_black")
    cprint("5. Comparing sophisticated growth with different growth rates (p3)", "green", "on_black")
    cprint("6. Population size at each fission event (p4)", "green", "on_black")
    cprint("7. Population growth over one day (p5)", "green", "on_black")
    menu_num = quit(input(colored("Enter your choice: ", "blue", "on_black"))) # Get the user's choice
    while not menu_num.isnumeric() or int(menu_num) < 1 or int(menu_num) > 7:
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
    if text.lower() == "menu": # If the user types menu, the program will return to the main menu
        change_menu_bool = True
    else:
        return text # If the user does not type menu, the program will continue

def convert_time(value, original_unit, target_unit, calculate_percentage): # Convert time units
    if not calculate_percentage:
        final_value = value * time_units[original_unit] / time_units[target_unit] # Convert the value to seconds and then to the target unit
    else:
        final_value = (value / time_units[original_unit]) * time_units[target_unit] / 100 # Adjusted percentage calculation
    return final_value # Return the final value in the target unit

def is_float(value): # Check if the value is a float
    if value == None:
        return False # If the value is None, return False
    try:
        value = value.replace(" ", "")
        float(value) # Try to convert the value to a float
        return float(value.replace(" ", "")) # Return the value as a float
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
    if input_time == None or len(input_time.split(" ")) == 1: # Check if the input is None or empty
        cprint("Please enter a valid time.", "red", "on_black")
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

def growth_inputs(target, population_increase, one_day):
    if change_menu_bool == False:
        initial_population = is_float(change_menu(quit(input(colored("Enter the initial population: ", "blue", "on_black"))))) # Get the initial population from the user
        while initial_population == False and change_menu_bool == False: # If the input is not a number, ask for the input again
            initial_population = is_float(change_menu(quit(input(colored("Enter the initial population: ", "blue", "on_black"))))) # Ask for the input again
    if change_menu_bool == False and not one_day:
        growth_rate = is_percentage(change_menu(quit(input(colored("Enter the growth rate: ", "blue", "on_black"))))) # Above comments apply to the other inputs as well
        while growth_rate == False and change_menu_bool == False:
            growth_rate = is_percentage(change_menu(quit(input(colored("Enter the growth rate: ", "blue", "on_black")))))
    if change_menu_bool == False:
        growth_time_period = input_time_error_check(change_menu(quit(input(colored(f"Enter the time for one growth period: ", "blue", "on_black")))))
        while growth_time_period == False and change_menu_bool == False:
            growth_time_period = input_time_error_check(change_menu(quit(input(colored(f"Enter the time for one growth period: ", "blue", "on_black")))))
    if change_menu_bool == False and not target and not population_increase and not one_day:
        growth_time = input_time_error_check(change_menu(quit(input(colored("Enter the amount of time to project into the future: ", "blue", "on_black")))))
        while growth_time == False and change_menu_bool == False:
            growth_time = input_time_error_check(change_menu(quit(input(colored("Enter the amount of time to project into the future: ", "blue", "on_black")))))
        if change_menu_bool == False:
            return [initial_population, growth_rate, growth_time_period, growth_time] # Return the inputs as a list
    if change_menu_bool == False and not target and population_increase and not one_day:
        growth_time = change_menu(quit(input(colored(f"Enter the amount of time to project into the future (enter 'target' for target population input): ", "blue", "on_black"))))
        while change_menu_bool == False and growth_time.lower() != "target" and input_time_error_check(growth_time) == False:
            growth_time = change_menu(quit(input(colored(f"Enter the amount of time to project into the future (enter 'target' for target population input): ", "blue", "on_black"))))
        if growth_time.lower() == "target":
            target = True
        else:
            return [initial_population, growth_rate, growth_time_period, input_time_error_check(growth_time)] # Return the inputs as a list
    if change_menu_bool == False and target and not one_day:
        target_population = is_float(change_menu(quit(input(colored("Enter the target population: ", "blue", "on_black")))))
        while target_population == False and change_menu_bool == False:
            target_population = is_float(change_menu(quit(input(colored("Enter the target population: ", "blue", "on_black")))))
        if change_menu_bool == False:
            return [initial_population, growth_rate, growth_time_period, target_population] # Return the inputs as a list
    if change_menu_bool == False:
        return [initial_population, growth_time_period] # Return the inputs as a list if not already

def naive_growth(is_comparison): # Naive growth function (simple growth)
    global change_menu_bool
    # N(t) = N(0) + (N(0) * r * t) where N(t) is the population at time t, N(0) is the initial population, r is the growth rate, and t is the time
    if not is_comparison:
        cprint("\nNaive Growth (simple growth) Calculator!", "green", "on_black")
        inputs = growth_inputs(False, False, False) # Get the inputs from the user
    else:
        inputs = is_comparison
    # Calculate the simple growth
    if change_menu_bool == False:
        cprint(f"Calculating naive (simple) growth of {inputs[0]} with a growth rate of {inputs[1]*100}% every {inputs[2][0]} {inputs[2][1]}(s), over a period of {inputs[3][0]} {inputs[3][1]}(s)...", "green", "on_black")
        total_time_periods = math.floor(convert_time(inputs[3][0], inputs[3][1], inputs[2][1], False) / inputs[2][0]) # Calculate how many growth periods are in the total time
        final_amount = inputs[0] + (inputs[0] * inputs[1] * total_time_periods) # Calculate the final amount using the formula N(t) = N(0) + (N(0) * r * t)
        return [inputs[0], inputs[1], inputs[2], inputs[3], final_amount] # Return the final amount

def sophisticated_growth(is_comparison, target, is_self_comparison, population_increase): # Sophisticated growth function (exponential growth)
    global change_menu_bool
    # N(t) = N(0) * (1 + r)^t where N(t) is the population at time t, N(0) is the initial population, r is the growth rate, and t is the time
    if not is_comparison and not target and not is_self_comparison and not population_increase and change_menu_bool == False:
        cprint("\nSophisticated Growth (exponential growth) Calculator!", "green", "on_black")
        inputs = growth_inputs(False, False, False) # Get the inputs from the user
    elif is_self_comparison != False and change_menu_bool == False:
        cprint(f"\nSophisticated Growth Comparison, inputs for scenario {is_self_comparison}!", "green", "on_black")
        inputs = growth_inputs(False, False, False) # Get the inputs from the user
    elif is_comparison != False:
        inputs = is_comparison
    elif target != False:
        inputs = target
    elif population_increase != False:
        inputs = population_increase
    time_taken = 0
    growth_amounts = [] # List to store the growth amounts at each time period
    starting_amount = inputs[0]
    final_amount = inputs[0] # Set the final amount to the initial population
    # Calculate the exponential growth
    if change_menu_bool == False and not target:
        total_time_periods = math.floor(convert_time(inputs[3][0], inputs[3][1], inputs[2][1], False) / inputs[2][0]) # Calculate how many growth periods are in the total time
        if population_increase == False:
            cprint(f"Calculating sophisticated (exponential) growth of {inputs[0]} with a growth rate of {inputs[1]*100}% every {inputs[2][0]} {inputs[2][1]}(s), over a period of {inputs[3][0]} {inputs[3][1]}(s)...", "green", "on_black")
            final_amount = inputs[0] * (1 + inputs[1])**total_time_periods
        elif population_increase != False:
            for i in range(total_time_periods):
                final_amount = final_amount * (1 + inputs[1])
                time_taken += inputs[2][0]
                growth_amounts.append([f"{time_taken} {inputs[2][1]}(s)", starting_amount, final_amount - starting_amount, final_amount])
                starting_amount = final_amount
        return [inputs[0], inputs[1], inputs[2], inputs[3], final_amount, growth_amounts]
    elif change_menu_bool == False and target != False:
        if not population_increase:
            growth_amounts = [[f"{time_taken} {inputs[2][1]}", final_amount]] # List to store the growth amounts at each time period
        while final_amount < inputs[3]:
            final_amount = final_amount * (1 + inputs[1])
            time_taken += 1*inputs[2][0]
            if not population_increase:
                growth_amounts.append([f"{time_taken} {inputs[2][1]}(s)", final_amount]) # Append the amount to the list
            elif population_increase != False:
                growth_amounts.append([f"{time_taken} {inputs[2][1]}(s)", starting_amount, final_amount - starting_amount, final_amount]) # Append the amount to the list
            starting_amount = final_amount
        return [inputs[0], inputs[1], inputs[2], inputs[3], time_taken, final_amount, growth_amounts] # Return the final amount and the time taken to reach the target population

def compare_growth(model_1, model_2):
    global change_menu_bool
    # Compare naive and sophisticated growth
    if model_1 == model_2 and change_menu_bool == False:
        cprint(f"\nSophisticated Growth vs Sophisticated Growth Comparison!", "green", "on_black")
        model_1_result = model_1(False, False, 1, False)
        if change_menu_bool == False:
            model_2_result = model_2(False, False, 2, False)
    elif model_1 != model_2 and change_menu_bool == False:
        cprint(f"\nNaive Growth vs Sophisticated Growth Comparison!", "green", "on_black")
        inputs = growth_inputs(False, False, False) # Get the inputs from the user    
        model_1_result = model_1(inputs) # Get the result from the naive growth function
        model_2_result = model_2(inputs, False, False, False) # Get the result from the sophisticated growth function
    if change_menu_bool == False:
        if model_1 == model_2:
            cprint(f"Comparing Sophisticated Growth of {model_1_result[0]} with a growth rate of {model_1_result[1]*100}% every {model_1_result[2][0]} {model_1_result[2][1]}(s), over a period of {model_1_result[3][0]} {model_1_result[3][1]}(s)...", "green", "on_black")
            cprint(f"VS Sophisticated Growth of {model_2_result[0]} with a growth rate of {model_2_result[1]*100}% every {model_2_result[2][0]} {model_2_result[2][1]}(s), over a period of {model_2_result[3][0]} {model_2_result[3][1]}(s)...", "green", "on_black")
            return [["Sophisticated Growth", model_1_result[4]], ["Sophisticated Growth", model_2_result[4]]] # Create a table to display the results
        else:
            cprint(f"Comparing Naive and Sophisticated growth!", "green", "on_black")
            return [["Naive Growth", model_1_result[4]], ["Sophisticated Growth", model_2_result[4]]]

def time_to_target_population():
    global change_menu_bool
    # Calculate the time taken to reach a target population
    cprint("\nProjected Time Until Target Population is Reached!", "green", "on_black")
    inputs = growth_inputs(True, False, False) # Get the inputs from the user
    time_to_target_result = sophisticated_growth(False, inputs, False, False)
    if change_menu_bool == False:
        cprint(f"Calculating the time taken to reach a target population of {inputs[3]} with an initial population of {inputs[0]} and a growth rate of {inputs[1]*100}% every {inputs[2][0]} {inputs[2][1]}(s)...", "green", "on_black")
        return time_to_target_result # Return the time taken to reach the target population

def population_increase():
    global change_menu_bool
    # Calculate the population size at each fission event
    cprint("\nPopulation Size at Each Fission Event!", "green", "on_black")
    inputs = growth_inputs(False, True, False) # Get the inputs from the user
    if type(inputs[3]) == list:
        option_type = "growth_time"
    elif type(inputs[3]) == float:
        option_type = "target"
    if option_type == "growth_time":
        population_increase_result = sophisticated_growth(False, False, False, inputs) # Get the result from the sophisticated growth function
    elif option_type == "target":
        population_increase_result = sophisticated_growth(False, inputs, False, inputs)
    return population_increase_result, option_type # Return the population size at each fission event

def one_day_growth():
    global change_menu_bool
    cprint("\nPopulation growth over one day", "green", "on_black")
    inputs = growth_inputs(False, False, True) # Get the inputs from the user
    if change_menu_bool == False:
        inputs = [inputs[0], convert_time(100, "day", inputs[1][1], True), inputs[1], [1, "day"]]
        one_day_growth_result = sophisticated_growth(False, False, False, inputs) # Get the result from the sophisticated growth function
        return one_day_growth_result # Return the population growth over one day

welcome()
while True:
    menu()
    while menu_num == 1: # If the user selects menu 1
        result = naive_growth(False) # Call the naive growth function
        if change_menu_bool == False: # If the user did not type menu, display the result
            print()
            cprint(f"Starting with an initial population of {result[0]}, growing simply at a rate of {result[1]*100}% every {result[2][0]} {result[2][1]}(s), over a total time of {result[3][0]} {result[3][1]}(s), the final population is projected to be {float(result[4])} bacteria.", "green", "on_black")
        if repeat_menu in false_inputs or change_menu_bool == True: # If the user does not want to repeat the menu or if they want to change the menu, break the loop
            break
    while menu_num == 2: # Same as above comments
        result = sophisticated_growth(False, False, False, False)
        if change_menu_bool == False:
            print()
            cprint(f"Starting with an initial population of {result[0]}, growing exponentially at a rate of {result[1]*100}% every {result[2][0]} {result[2][1]}(s), over a total time of {result[3][0]} {result[3][1]}(s), the final population is projected to be {float(result[4])} bacteria.", "green", "on_black")
        if repeat_menu in false_inputs or change_menu_bool == True:
            break
    while menu_num == 3:
        result = compare_growth(naive_growth, sophisticated_growth)
        if change_menu_bool == False:
            print()
            cprint(tabulate.tabulate(result, headers=["Growth Type", "Final Population"]), "green", "on_black") # Display the results in a table
        if repeat_menu in false_inputs or change_menu_bool == True:
            break
    while menu_num == 4:
        result = time_to_target_population()
        if change_menu_bool == False:
            print()
            cprint(f"The increments of growth are as follows:", "green", "on_black")
            cprint(tabulate.tabulate(result[6], headers=["Time Period", "Population"]), "green", "on_black") # Display the growth amounts at each time period in a table
            cprint(f"Starting with an initial population of {result[0]}, growing exponentially at a rate of {result[1]*100}% every {result[2][0]} {result[2][1]}(s), the time taken to reach a target population of {result[3]} is {result[4]} {result[2][1]}(s).", "green", "on_black")
        if repeat_menu in false_inputs or change_menu_bool == True:
            break
    while menu_num == 5:
        result = compare_growth(sophisticated_growth, sophisticated_growth)
        if change_menu_bool == False:
            print()
            cprint(tabulate.tabulate(result, headers=["Growth Type", "Final Population"]), "green", "on_black")
        if repeat_menu in false_inputs or change_menu_bool == True:
            break
    while menu_num == 6:
        result, option_type = population_increase()
        if change_menu_bool == False:
            print()
            cprint(f"The increments of growth are as follows:", "green", "on_black")
            cprint(tabulate.tabulate(result[-1], ["Time", "Initial Population", "New Bacteria", "Final population"]), "green", "on_black")
            if option_type == "growth_time":
                cprint(f"Starting with an initial population of {result[0]}, growing exponentially at a rate of {result[1]*100}% every {result[2][0]} {result[2][1]}(s), over a total time of {result[3][0]} {result[3][1]}(s), the final population is projected to be {float(result[4])} bacteria.", "green", "on_black")
            elif option_type == "target":
                cprint(f"Starting with an initial population of {result[0]}, growing exponentially at a rate of {result[1]*100}% every {result[2][0]} {result[2][1]}(s), the time taken to reach a target population of {result[3]} is {result[4]} {result[2][1]}(s).", "green", "on_black")
        if repeat_menu in false_inputs or change_menu_bool == True:
            break
    while menu_num == 7:
        result = one_day_growth()
        if change_menu_bool == False:
            print()
            cprint(f"The increments of growth are as follows:", "green", "on_black")
            cprint(tabulate.tabulate(result[5], ["Time", "Initial Population", "New Bacteria", "Final population"]), "green", "on_black")
            cprint(f"Starting with an initial population of {result[0]}, growing exponentially at a rate of {result[1]*100}% every {result[2][0]} {result[2][1]}(s), over a total time of {result[3][0]} {result[3][1]}(s), the final population is projected to be {float(result[4])} bacteria.", "green", "on_black")
        if repeat_menu in false_inputs or change_menu_bool == True:
            break