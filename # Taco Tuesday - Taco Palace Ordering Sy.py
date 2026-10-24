# Taco Tuesday - Taco Palace Ordering System


def print_menu():
    """Print the Taco Palace menu."""
    print("\nTaco Palace Menu")
    print("1. Taco - $3.50")
    print("2. Burrito - $7.25")
    print("3. Nachos - $6.00")
    print("4. Soft Drink - $2.25")
    print("5. Quit")


def get_price(selection):
    """Return the price of the selected food item."""
    if selection == 1:
        return 3.50
    elif selection == 2:
        return 7.25
    elif selection == 3:
        return 6.00
    elif selection == 4:
        return 2.25
    else:
        return 0.00


def get_item_name(selection):
    """Return the name of the selected food item."""
    if selection == 1:
        return "Taco"
    elif selection == 2:
        return "Burrito"
    elif selection == 3:
        return "Nachos"
    elif selection == 4:
        return "Soft Drink"
    else:
        return ""


def item_with_article(item_name):
    """Add an article when it makes sense for the item name."""
    if item_name == "Nachos":
        return item_name
    else:
        return "a " + item_name


def format_order(order_list):
    """Format the list of ordered items into a readable sentence."""
    if len(order_list) == 0:
        return "nothing"
    elif len(order_list) == 1:
        return item_with_article(order_list[0])
    elif len(order_list) == 2:
        return item_with_article(order_list[0]) + " and " + item_with_article(order_list[1])
    else:
        formatted_items = ""
        for item in order_list[:-1]:
            formatted_items += item_with_article(item) + ", "
        formatted_items += "and " + item_with_article(order_list[-1])
        return formatted_items


def main():
    ordered_items = []
    total_due = 0.00

    print("Welcome to Taco Palace, please view the menu below and enter the number that represents your selection.")

    while True:
        print_menu()
        selection = int(input("Enter your selection: "))
        print("User entered:", selection)

        if selection == 5:
            break
        elif selection >= 1 and selection <= 4:
            item_name = get_item_name(selection)
            item_price = get_price(selection)

            print("You have selected " + item_with_article(item_name) + ".")

            ordered_items.append(item_name)
            total_due += item_price
        else:
            print("Invalid selection. Please enter a number from 1 to 5.")

    print("\nYou ordered " + format_order(ordered_items) + ".")
    print("Your total is $" + format(total_due, ".2f"))


main()