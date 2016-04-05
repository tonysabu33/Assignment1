""" CP5632 Assignment 1 - 2016
    Items For Hire - Solution
    Tony Sabu
    20-03-2016

Pseudocode:

display welcome message with author name
import csv file

function  main()
    display menu
    get choice
    while choice is not 'q'
        if choice is 'l'
            display all items with details after a message
            returns to menu
        else if choice is 'h'
            display items available to hire with details
            gets the number of the item to hire
                if that item number is there in the list
                    item hired message
                else if that item number is not in the list
                    shows that the item is not available to hire
                else
                    shows that no items available to hire
            returns to menu
        else if choice is 'r'
            display items on hire with details
            gets the number of the item to return
                if that item number is there in the list
                    item returned message
                else if that item number is not in the list
                    shows that the item is not hired
                else
                    shows that no more item to return
            returns to menu
        else
            gets the item name
            gets the item description
            gets the price for the item to hire
            shows message about the item availability with item details
            returns to menu
   quits
"""

ITEMS = open('item.csv')
AVL_ITEMS = [0, 3, 4]
HIR_ITEMS = [1, 2]
TOTAL_ITEMS = AVL_ITEMS + HIR_ITEMS

NAME = []
DESCRIPTION = []
PRICE = []

for line in ITEMS:
    parts = line.strip().split(",")
    NAME.append(parts[0])
    DESCRIPTION.append(parts[1])
    PRICE.append(float(parts[2]))
ITEMS.close()
Menu = "\nMenu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd an item\n(Q)uit"


def main():
    print("Welcome")
    print("Written by Tony Sabu")

    print(Menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            list_of_items()
        elif choice == "R":
            return_item()
        elif choice == "H":
            hire_item()
        elif choice == "A":
            add_item()
        else:
            print("Invalid menu choice.")
        print(Menu)
        choice = input(">>> ").upper()

    print('{} items saved to item.csv'.format(len(AVL_ITEMS + HIR_ITEMS)))


def list_of_items():
    print('All items on file (* indicates item is currently out)')
    full_item = AVL_ITEMS + HIR_ITEMS
    for number in sorted(full_item):
        if number in AVL_ITEMS:
            print("{} - {:15} {:35} = $ {:>2.2f}".format(number, NAME[number], '(' + DESCRIPTION[number] + ')',
                                                         PRICE[number]))
        else:
            print("{} - {:15} {:35} = $ {:>2.2f} *".format(number, NAME[number], '(' + DESCRIPTION[number] + ')',
                                                           PRICE[number]))


# list_of_items()


def hire_item():

    if len(AVL_ITEMS) == 0:
        print('No item to hire')

    else:
        for number in AVL_ITEMS:
            print("{} - {} {} = $ {}".format(number, NAME[number], DESCRIPTION[number], PRICE[number]))

        while True:
            try:
                hire = int(input('enter the number of an item to hire:'))
            except ValueError:
                print('Invalid input; enter a number')
                continue

            else:
                print("{} hired for ${}".format(NAME[hire], PRICE[hire]))
                HIR_ITEMS.append(hire)
                AVL_ITEMS.remove(hire)
                break


def return_item():
    if len(HIR_ITEMS) == 0:
        print('No items are currently on hire')
    else:
        for number in HIR_ITEMS:
            print("{} - {} {} = $ {}".format(number, NAME[number], DESCRIPTION[number], PRICE[number]))
    while True:
        try:
            rt_item = int(input('enter the number of an item to return:'))
        except ValueError:
            print('Invalid input; enter a number')
            continue
        else:
            print("{} returned".format(NAME[rt_item]))
            HIR_ITEMS.remove(rt_item)
            AVL_ITEMS.append(rt_item)
            break


def add_item():
    it_name = input('Item name:')
    description = input('Description:')
    while True:
        try:
            price = float(input('Price per day:'))
        except ValueError:
            print('Enter a valid number')
            continue
        else:
            NAME.append(it_name)
            DESCRIPTION.append(description)
            PRICE.append(price)
            print("{} ({}), ${} now available for hire".format(it_name, description, price))
            if max(AVL_ITEMS) > max(HIR_ITEMS):
                AVL_ITEMS.append(max(AVL_ITEMS) + 1)
            else:
                AVL_ITEMS.append(max(HIR_ITEMS) + 1)
            break
    new_file_data = ""
    for i in AVL_ITEMS + HIR_ITEMS:
        new_file_data += NAME[i]
        new_file_data += DESCRIPTION[i]
        new_file_data += str(PRICE[i])
        # new_file_data +=
        new_file_data += "\n"
    print(repr(new_file_data))
    ITEMS = open("item.csv", 'w')
    ITEMS.write(new_file_data)
    ITEMS.close()


main()
