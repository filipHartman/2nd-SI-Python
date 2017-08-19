# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification
import csv


# Displays the inventory.
def display_inventory(inventory):
    total_items = 0
    print("Inventory: ")
    for item in inventory.keys():
        print(inventory[item], item)
        total_items += int(inventory[item])
    print("Total number of items: ", str(total_items))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for loot in added_items:
        if loot in inventory:
            inventory[loot] += 1
        else:
            inventory[loot] = 1
    return inventory


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    max_characters_number = 0
    total_items = 0

    for item in inventory.keys():
        if int(max_characters_number) < len(item):
            max_characters_number = len(item)
    print("Inventory: ")
    print("{:{align}7} {:4} {:{align}{width}}".format(
        "count", "", "item name", align=">", width=max_characters_number))
    print("{:_>{width}}".format("", width=max_characters_number+13))

    if order == "count,desc":
            desc_inventory = sorted(list(zip(inventory.values(), inventory.keys())))
            for item in range(1, len(desc_inventory)+1):
                print("{:{align}7} {:4} {:{align}{width}}".format(
                    desc_inventory[-item][0], "", desc_inventory[-item][1], align=">", width=max_characters_number))
                total_items += int(desc_inventory[-item][0])

    elif order == "count,asc":
        asc_inventory = sorted(list(zip(inventory.values(), inventory.keys())))
        for item in range(0, len(asc_inventory)):
            print("{:{align}7} {:4} {:{align}{width}}".format(
                asc_inventory[item][0], "", asc_inventory[item][1], align=">", width=max_characters_number))
            total_items += int(asc_inventory[item][0])

    else:
        for item in inventory:
            print("{:{align}7} {:4} {:{align}{width}}".format(
                inventory[item], "", item, align=">", width=max_characters_number))
            total_items += inventory[item]

    print("{:_>{width}}".format("", width=max_characters_number+13))
    print("Total number of items: " + str(total_items))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename, "r") as imported_file:
        csv_inventory = csv.reader(imported_file)

        imported_inventory = []

        for line in csv_inventory:
            for item in line:
                imported_inventory.append(item)
        add_to_inventory(inventory, imported_inventory)


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    with open(filename, "w") as exported_file:
        exported_inventory = csv.writer(exported_file, delimiter=',')
        exported_list = []
        for item in inventory:
            for amount_of_item in range(inventory[item]):
                exported_list.append(item)
        exported_inventory.writerow(exported_list)
# Main function sets initial variables and stores rest of the functions


def main():
    pass
