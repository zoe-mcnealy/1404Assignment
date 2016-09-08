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
    get input from user
        flow throuhg the list until the user input is found
            change the is_complete to 'c'
        if user input isn't found in the list
            display and error message and aske the user for input again.

valid_string_check
    get input passed into function
        error check to make sure the input isn't blank
        return valid string

valid_num_check
    get input passed into function
        error check to make sure the input can be converted to a float
            if not display an error message and ask for input again
    error check to make sure the input if >= 0
            if not display an error message and ask for input again
    return valid int

read_file
    open file
    import data from the csv file into various lists
    close file

write_file
    open file and clear data
    export lists into file
    close file

"""



shopping_items= []
item_costs = []
priority_num = []
is_completed = []
MENU = "Please Choose and Option:\nR - List required items\nC - List completed Items\nA - Add a new item\nM - Mark an item as completed\nQ - Quit"


def  main():
    WELCOME_MENU = "Shopping List 1.0 - By Zoe McNealy"
    lists = read_file()
    print(WELCOME_MENU)
    print(MENU)
    choice = input("").upper()

    while choice != "Q":

        if choice == "R":
            print_listed_items (lists,"Required Items", "r")
        elif choice == "C":
            print_listed_items(lists,"Completed Items", "c")
        elif choice == "A":
            add_items(lists)
        elif choice == "M":
            modify_status(lists)
        else:
            print("Invalid Choice. Please choose again.")

        print(MENU)
        choice= input("").upper()
    print('Your changes have been saved. Goodbye')
    write_to_file(lists)


def print_listed_items(lists,list_title, status):
#print items in a formatted list
    total_cost = 0
    num_items = 0
    print(list_title + ": ")
    for i in range(0, len(lists["names"])):
        if lists["status"][i] == status.lower():
            print(i , ". {:30s} ${:.2f} \t({})".format(lists["names"][i], lists["costs"][i], lists["priority"][i]))
            total_cost = total_cost + lists["costs"][i]
            num_items = num_items + 1


    print("Total expected price for {} items : ${:.2f}".format(num_items, total_cost))

def add_items(lists):
# add a new item to various lists
    new_item =  input("Item Name: ")
    new_item_name = valid_string_check(new_item,"Item Name")
    lists["names"].append(new_item_name)

    new_item = input("Price: ")
    new_item_price = valid_num_check(new_item, "Item Price")
    lists["costs"].append(new_item_price)

    new_item = input("Priority Must be 1, 2 or 3: ")
    new_item_priority = valid_string_check(new_item, "Item Priority. Must be 1, 2 or 3.")
    lists["priority"].append(new_item_priority)

    lists["status"].append('r')

def modify_status(lists):
# modify the is_completed variable to make the item as complete
    valid_int = False
    while valid_int == False:
        print_listed_items(lists,"Required Items", 'r')
        status_change = input("Enter the number of the item to mark as completed")
        try:
            status_change = int(status_change)
            if status_change < len(lists["names"]) and status_change >= 0:
                lists["status"][int(status_change)] = 'c'
                valid_int = True
                print("Status Changed")
            else:
                print("Invalid number entered. Please try again")
        except ValueError:
             print("That is not a number. Please try again")

    while int(status_change) > len(lists["names"]):
        print("Invalid option. Please try again")
        print_listed_items("Required Items", 'r')
        status_change = input("Enter the number of the item to mark as completed")

def valid_string_check(user_input, variable_name):
# used to validate any str user_input
    user_input = user_input.strip( )
    while len(user_input) == 0:
        print(variable_name + " cannot be blank")
        user_input = input("Please Try Again: ")
    return user_input

def valid_num_check(user_input, variable_name):
# used to validate any int user_input
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
    return user_input

def read_file():
# Open file and read data into various lists
    lists = {"names": [], "costs": [], "priority": [], "status": []}
    items_list = []
    infile = open("items.csv", "r")
    for line in infile:
        line = line.strip("\n")
        items_list = line.split(',')
        lists["names"].append(items_list[0])
        lists["costs"].append(float(items_list[1]))
        lists["priority"].append(int(items_list[2]))
        lists["status"].append(items_list[3])
    infile.close()
    return lists


def write_to_file(lists):
# write to the csv file after quitting
    outfile = open("items.csv", "w")
    for i in range(0, len(lists["names"])):
        outfile.write(( "{},{},{},{}\n".format(lists["names"][i], lists["costs"][i], lists["priority"][i], lists["status"][i])))
    outfile.close()



main()
