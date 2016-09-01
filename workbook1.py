
WELCOME_MENU = "Shopping List 1.0 - By Zoe McNealy"
items_list = []
shopping_items= []
item_costs = []
priority_num = []
is_completed = []
total_cost = 0
num_items = 0

MENU = "Please Choose and Option:\nR - List required items\nC - List completed Items\nA - Add a new item\nM - Mark an item as completed\nQ - Quit"
print(MENU)
choice = input("").upper()

while choice != "Q":
    if choice == "R":

        infile = open("items.csv","r")
        for line in infile:
            line= line.strip("\n")
            items_list = line.split(',')
            shopping_items.append(items_list[0])
            item_costs.append(float(items_list[1]))
            priority_num.append(int(items_list[2]))
            is_completed.append(items_list[3])
        infile.close()
        print("Required Items:")
        for i in range(0,len(shopping_items)):
            if is_completed[i] == "r":
                print(1,". {}\t ${:.2f} ({})".format(shopping_items[i],item_costs[i],priority_num[i]))
                total_cost = total_cost + item_costs[i]
                num_items = num_items + 1

        print("Total expected price for {} items : ${:.2f}".format(num_items,total_cost))
        print(MENU)
        choice = input("").upper()
    elif choice == "C":
        infile = open("items.csv", "r")
        for line in infile:
            line = line.strip("\n")
            items_list = line.split(',')
            shopping_items.append(items_list[0])
            item_costs.append(float(items_list[1]))
            priority_num.append(int(items_list[2]))
            is_completed.append(items_list[3])
        infile.close()
        print("Completed Items:")
        total_cost = 0
        for i in range(0, len(shopping_items)):
            if is_completed[i] == "c":
                print(i, ". {:15s} ${:6.2f} ({})".format(shopping_items[i], item_costs[i], priority_num[i]))
                total_cost = total_cost + item_costs[i]
                num_items = num_items + 1

        print("Total expected price for {} items : ${:.2f}".format(num_items, total_cost))
        print(MENU)
        choice = input("").upper()
    elif choice == "A":
        print("TO DO")
    elif choice == "M":
        print("TO DO")
    else:
            print("Invalid Choice. Please choose again.")
            choice = input("R - List required items\n C - List completed Items\n A - Add a new item\n Q - Quit")



