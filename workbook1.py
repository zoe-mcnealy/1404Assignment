
WELCOME_MENU = "Shopping List 1.0 - By Zoe McNealy"
items_list = []
shopping_items= []
item_costs = []
priority_num = []
is_completed = []

MENU = "Please Choose and Option:\nR - List required items\nC - List completed Items\nA - Add a new item\nM - Mark an item as completed\nQ - Quit"
print(MENU)
choice = input("").upper()

#while choice != "Q":
if choice == "R":
    infile = open("items.csv","r")
    for line in infile:
        line= line.strip("\n")
        items_list = line.split(',')
        shopping_items.append(items_list[0])
        item_costs.append(items_list[1])
        priority_num.append(items_list[2])
        is_completed.append(items_list[3])
#print(shopping_items)
#print(item_costs)
#print(priority_num)
#print(is_completed)
    for i in range(0,len(shopping_items)):
        print(i+1 ,". {}\t ${:.5} ({})".format(shopping_items[i],item_costs[i],priority_num[i]))
elif choice == "C":
    print("TO DO")
elif choice == "A":
    print("TO DO")
elif choice == "M":
    print("TO DO")
else:
        print("Invalid Choice. Please choose again.")
        choice = input("R - List required items\n C - List completed Items\n A - Add a new item\n Q - Quit")



