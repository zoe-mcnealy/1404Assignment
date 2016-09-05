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
            listed_items ("Required Items", "r")
        elif choice == "C":
            listed_items("Completed Items", "c")
        elif choice == "A":
            add_items()
        elif choice == "M":
            print("TO DO")
        else:
            print("Invalid Choice. Please choose again.")
            choice = input(print(MENU))
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
    print(MENU)
    choice = input("").upper()
    return choice
    print("Total expected price for {} items : ${:.2f}".format(num_items, total_cost))
    print(MENU)

def add_items():
    add_new_item = []
    new_item =  input("Item Name: ")
    new_item_name = valid_string_check(new_item,"Item Name")
    add_new_item.append(new_item_name)

    new_item = input("Price: ")
    new_item_price = valid_num_check(new_item, "Item Price")
    add_new_item.append(new_item_price)

    new_item = input("Priority: ")
    new_item_priority = valid_string_check(new_item, "Item Priority. Must be 1, 2 or 3.")
    add_new_item.append(new_item_priority)

    add_new_item.append('r')

    right_to_file(add_new_item)

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
    while user_input <= 0:
        print(variable_name + " must be >= $0")
        user_input = input(variable_name + ": ")

def print_items():
    print("Required Items:")
    for i in range(0, len(shopping_items)):
        if is_completed[i] == "r":
            print(1, ". {}\t ${:.2f} ({})".format(shopping_items[i], item_costs[i], priority_num[i]))
            total_cost = total_cost + item_costs[i]
            num_items = num_items + 1

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
