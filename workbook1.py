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

valid_string

"""



items_list = []
shopping_items= []
item_costs = []
priority_num = []
is_completed = []
MENU = "Please Choose and Option:\nR - List required items\nC - List completed Items\nA - Add a new item\nM - Mark an item as completed\nQ - Quit"


def  main():
    WELCOME_MENU = "Shopping List 1.0 - By Zoe McNealy"
    read_file()
    print(WELCOME_MENU)
    print(MENU)
    choice = input("").upper()

    while choice != "Q":

        if choice == "R":
            print_listed_items ("Required Items", "r")
        elif choice == "C":
            print_listed_items("Completed Items", "c")
        elif choice == "A":
            add_items()
        elif choice == "M":
            modify_status()
        else:
            print("Invalid Choice. Please choose again.")

        print(MENU)
        choice= input("").upper()
    print('Your changes have been saved. Goodbye')


def print_listed_items(list_title, status):
    total_cost = 0
    num_items = 0
#    sort_items()
    print(list_title + ": ")
    for i in range(0, len(shopping_items)):
        if is_completed[i] == status.lower():
            print(i , ". {:30s} ${:.2f} ({})".format(shopping_items[i], item_costs[i], priority_num[i]))
            total_cost = total_cost + item_costs[i]
            num_items = num_items + 1


    print("Total expected price for {} items : ${:.2f}".format(num_items, total_cost))

#add a new item to various
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


#modify the is_completed variable
def modify_status():
    valid_int = False
    while valid_int == False:
        print_listed_items("Required Items", 'r')
        status_change = input("Enter the number of the item to mark as completed")
        try:
            status_change = int(status_change)
            if status_change < len(shopping_items) and status_change >= 0:
                is_completed[int(status_change)] = 'c'
                valid_int = True
            else:
                print("Invalid number entered. Please try again")
        except ValueError:
             print("That is not a number. Please try again")

    while int(status_change) > len(shopping_items):
        print("Invalid option. Please try again")
        print_listed_items("Required Items", 'r')
        status_change = input("Enter the number of the item to mark as completed")



#used to validate any str user_input
def valid_string_check(user_input, variable_name):
    user_input = user_input.strip( )
    while len(user_input) == 0:
        print(variable_name + " cannot be blank")
        user_input = input("Please Try Again: ")
    return user_input

#used to validate any int user_input
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
    return user_input

#Open file and read data into various lists
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

#write to the csv file
def write_to_file(add_list):
    outfile = open("items.csv", "a")
    for i in add_list:
        outfile.write(str(i)+ ',')
    outfile.write("\n")
    outfile.close()


def sort_items():
    #http://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
    shopping_items = [si for p,si in sorted(zip(priority_num,shopping_items))]
    item_costs = [ic for p,ic in sorted(zip(priority_num,item_costs))]
    is_completed = [isc for p,isc in sorted(zip(priority_num,is_completed))]
    priority_num = sorted(priority_num)


main()
