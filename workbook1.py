"""Zoe McNealy  9 September 2016
BREIF PROGRAM DETAILS
LINK TO GitHub - https://github.com/zoe-mcnealy/1404Assignment

PSEUDOCODE

 Main Function
    Call function to load file and input data into list
    Display welcome
    Display menu
    get Input from user
    While the user doesn't choose to quit.
        If user chooses list required items
            Call a function to list items
        If user chooses list completed items
            Call a function to list items
        If user chooses to add another item
            Call a function to get input from user and add it to the existing lists
        If user chooses to modify the status of an item
            Call a function to get input from user and modify the status of the specified item
    If the user inputs none of these options, display an error message and ask for input again.

listed_items
    Goes through the list passed thought to the function
    Check the require/completed variable for each item on your list
    Print the items on the list with fit the require/completed variable which was passed into the function

add_item
    get item name from user
        error check
            call a string error checker
        add this item to a list
    get price from user
        error check
            call a float/int error checker function
        add this num to a list
    get priority from user
        error check
            call a float/int error checker function
        add this num to a list
    add status to list

modify_status



"""



items_list = []
shopping_items= []
item_costs = []
priority_num = []
is_completed = []
MENU = "Please Choose and Option:\nR - List required items\nC - List completed Items\nA - Add a new item\nM - Mark an item as completed\nQ - Quit"

#
def  main():
    WELCOME_MENU = "Shopping List 1.0 - By Zoe McNealy"
    read_file()
    print(WELCOME_MENU)
    print(MENU)
    choice = input("").upper()

    while choice != "Q":

        if choice == "R":
            listed_items ("Required Items", "r")
        elif choice == "C":
            listed_items("Completed Items", "c")
        elif choice == "A":
            add_items()
        elif choice == "M":
            modify_status()
        else:
            print("Invalid Choice. Please choose again.")
            choice = input(print(MENU))
        print(item_costs)
        print(MENU)

        choice= input("").upper()


def listed_items(list_title, status):
    total_cost = 0
    num_items = 0
    print(list_title + ": ")
    for i in range(0, len(shopping_items)):
        if is_completed[i] == status.lower():
            print(i , ". {}\t ${:.2f} ({})".format(shopping_items[i], item_costs[i], priority_num[i]))
            total_cost = total_cost + item_costs[i]
            num_items = num_items + 1

    print("Total expected price for {} items : ${:.2f}".format(num_items, total_cost))

def add_items():
    new_item =  input("Item Name: ")
    new_item_name = valid_string_check(new_item,"Item Name")
    shopping_items.append(new_item_name)

    new_item = input("Price: ")
    new_item_price = valid_num_check(new_item, "Item Price")
    item_costs.append(new_item_price)

    new_item = input("Priority Must be 1, 2 or 3: ")
    new_item_priority = valid_string_check(new_item, "Item Priority. Must be 1, 2 or 3.")
    priority_num.append(new_item_priority)

    is_completed.append('r')

def modify_status():
    listed_items("Required Items",'r')
    status_change= input("Enter the number of the item to mark as completed")
    valid_num_check(status_change, "Status of the item")
    if status_change in  range(0, len(shopping_items)):
        is_completed[status_change] = "c"
        print("OK")
    else:
        print("fail. the user input wasn't in the range")

def valid_string_check(user_input, variable_name):
    while len(user_input) == 0:
        print(variable_name + " cannot be blank")
        user_input = input("Please Try Again: ")
    return user_input


def valid_num_check(user_input, variable_name):
    valid_num = False
    while valid_num == False:
        try:
            user_input = float(user_input)
            valid_num = True
        except ValueError:
            print("Invalid entry. Please Try Again")
            user_input = input(variable_name + ": ")
    while user_input < 0:
        print(variable_name + " must be >= $0")
        user_input = input(variable_name + ": ")

def read_file():
    infile = open("items.csv", "r")
    for line in infile:
        line = line.strip("\n")
        items_list = line.split(',')
        shopping_items.append(items_list[0])
        item_costs.append(float(items_list[1]))
        priority_num.append(int(items_list[2]))
        is_completed.append(items_list[3])
    infile.close()

def right_to_file(add_list):
    outfile = open("items.csv", "a")
    for i in add_list:
        outfile.write(str(i)+ ',')
    outfile.write("\n")
    outfile.close()






main()
