infile = open("items.csv","r")
items_list = []
shopping_items= []
item_costs = []
priority_num = []
is_completed = []

for line in infile:
    line= line.strip("\n")
    items_list = line.split(',')
    shopping_items.append(items_list[0])
    item_costs.append(items_list[1])
    priority_num.append(items_list[2])
    is_completed.append(items_list[3])

print(shopping_items)
print(item_costs)
print(priority_num)
print(is_completed)

for i in range(0,len(shopping_items)):
    print("On your Shopping list there is:\n {} for ${:.5}. It is number {} on your list".format(shopping_items[i],item_costs[i],priority_num[i]))

