import csv

# Make sure this file is in the same folder as the .py file
FILE_NAME = "store_items.csv"
# Set the minimum stock
MIN_STOCK = 50

def read_csv():
    ''' () -> (list, list)

    Given a csv file_name, open and read the file.
    Return header and database:
     - The header is the list of the columns' names
     - The database is a list of lists that contains all the records.

    REQ: file_name has to be a valid .csv file with a header
    '''
    # Open the file given so we can read what's inside
    with open(FILE_NAME) as reader_file:
        # Read the file
        reader = csv.reader(reader_file)
        # Make it a list type, so it's easier for us to manage the data
        data = list(reader)
    # The first row of the data has the header
    # The rest of the data are records and will be stored in the database
    return (data[0], data[1:])


def write_to_csv(data):
    ''' (list) -> NoneType

    Write the data to the csv file.

    REQ: data must be a list of lists with consistent number of columns (in each row)
    '''
    # To make our database more organized, we will sort our csv file
    data.sort(key=lambda k: k[0])
    header = read_csv()[0]
    # Open the file given so we can write on it
    with open(FILE_NAME, 'w', newline="") as writer_file:
        writer = csv.writer(writer_file)
        # When we write the updated database back on the file, we need to
        # remember to add the header back in as well.
        writer.writerows([header] + data)


def get_item_price(item, colour):
    ''' (str, str) -> int

    Given an item and its colour, return the item's price.

    REQ: item and colour should be valid (the record should exist
    in the database)
    '''
    # Loop through every item in the database list (every row in the database)
    database = read_csv()[1]
    for item_record in database:
        # Every row in the database is a list itself, and we need to check
        # we find the right item and its colour
        if item_record[1] == item and item_record[2] == colour:
            # If you find the item, get the price and return it.
            # Make sure it's the right type!
            return int(item_record[3])


def get_item_quantity(item, colour):
    ''' (str, str) -> int

    Given an item and its colour, return how many of them are in stock.

    REQ: item and colour should be valid (the record should exist
    in the database)
    '''
    # Loop through every item in the database list (every row in the database)
    database = read_csv()[1]
    for item_record in database:
        # Every row in the database is a list itself, and we need to check
        # we find the right item and its colour
        if item_record[1] == item and item_record[2] == colour:
            # If you find the item, get the quantity and return it.
            # Make sure it's the right type!
            return int(item_record[4])


def add_item(category, name, colour, price, quantity):
    ''' (str, str, str, int, int) -> NoneType

    Given details for a new item, update the csv file.

    REQ: all input should be valid (the record should not already exist
    in the database)
    '''
    # Create a new record
    database = read_csv()[1]
    item_record = [category, name, colour, price, quantity]
    # Add the item record at the end of the database
    database += [item_record]
    # Write the new database to the file
    write_to_csv(database)
    print("Item added successfully!")


def remove_item(item, colour):
    ''' (str, str) -> NoneType

    Given an item and its colour, remove that item from the database
    and update the csv file.

    REQ: item and colour should be valid (the record should exist
    in the database)
    '''
    # Loop through every item in the database list a.k.a every row in the
    # database.
    database = read_csv()[1]
    for item_record in database:
        # Every row in the database is a list itself, and we need to check
        # we find the right item and its colour
        if item_record[1] == item and item_record[2] == colour:
            # If you find the record, remove it from the database
            database.remove(item_record)
            # As soon as you find it, you want to quit the loop
            print("Item removed successfully!")
            break
    # Write the new database to the file
    write_to_csv(database)


def update_price(item, colour, new_price):
    ''' (str, str, int) -> NoneType

    Given an item and its colour, update its record with the new_price.
    Once you make the update, don't forget to write it in the file.

    REQ: item and colour should be valid (the record should exist
    in the database) and the new_price has to be a number greater than 0.

    Example:
    >>> get_item_price("pants", "grey")
    60
    >>> update_price("pants", "grey", 70)
    Item price was successfully updated!
    >>> get_item_price("pants", "grey")
    70
    '''
    database = read_csv()[1]
    # Loop through every item in the database list a.k.a every row in the
    # database.
    for item_record in database:
        # Every row in the database is a list itself, and we need to check
        # we find the right item and its colour
        if item_record[1] == item and item_record[2] == colour:
            # If you find the record, replace it's current price
            # with the new price, remember the price is in index 3
            item_record[3] = new_price
            # As soon as you completed the update, you want to quit the loop
            print("Item price was successfully updated!")
            break
    # Write the new database to the file
    write_to_csv(database)


def purchase_items(item, colour, items_bought):
    ''' (str, str, int) -> NoneType

    Given an item, its colour and the amount of items purchased, update its
    record with the new updated inventory quantity left. The input items_bought
    is the amount of items the costumer has bought, so now we need to update it
    in our database. Once you make the update, don't forget to write it in
    the file.

    REQ: item and colour should be valid (the record should exist
    in the database) and items_bought has to be a number greater than 0 and
    less than the current quantity.

    Example:
    >>> get_item_quantity("pants", "grey")
    80
    >>> purchase_items("pants", "grey", 3)
    Item quantity was successfully updated!
    >>> get_item_quantity("pants", "grey")
    77
    '''
    database = read_csv()[1]
    # Loop through every item in the database list a.k.a every row in the
    # database.
    for item_record in database:
        # Every row in the database is a list itself, and we need to check
        # we find the right item and its colour
        if item_record[1] == item and item_record[2] == colour:
            # If you find the record, replace it's current quantity
            # remember the price is in index 4
            item_record[4] = int(item_record[4]) - items_bought
            # As soon as you completed the update, you want to quit the loop
            print("Item price was successfully updated!")
            break
    # Write the new database to the file
    write_to_csv(database)

def get_items_of_colour(colour):
    ''' (str) -> list

    Given a colour, return a list of all the items that are that colour.
    '''
    # Create a list to store the items that will be returned
    colour_items = []
    # Loop through every item in the database list (every row in the database)
    database = read_csv()[1]
    for item_record in database:
        # Every row in the database is a list itself, and we need to check
        # we find the right colour
        if item_record[2] == colour:
            # Add the item to the list
            colour_items.append(item_record[1])
    return colour_items

def get_colours_of_item(item):
    ''' (str) -> list

    Given an item, return a list of all its colours.
    '''
    # Create a list to store the items that will be returned
    item_colour = []
    # Loop through every item in the database list (every row in the database)
    database = read_csv()[1]
    for item_record in database:
        # Every row in the database is a list itself, and we need to check
        # we find the right item
        if item_record[1] == item:
            # Add the item to the list
            item_colour.append(item_record[2])
    return item_colour

def low_in_stock():
    ''' () -> list

    Return a list of all the items that have stock less than MIN_STOCK
    '''
    # Create a list to store the items that will be returned
    low_items = []
    # Loop through every item in the database list (every row in the database)
    database = read_csv()[1]
    for item_record in database:
        # Every row in the database is a list itself, and we need to check
        # we find the right item
        if int(item_record[4]) < MIN_STOCK:
            # Specify what colour it is
            item = item_record[2] + " " + item_record[1]
            # Add the item to the list
            low_items.append(item)
    return low_items

def shopping_list():
    ''' () -> list

    Return a list of all the items that the user has input.

    REQ: All inputs are existing records from the database.
    '''

    # Create a list to save all our shopping items
    shopping_list = []
    stop = False
    while(not stop):
        # Ask the user to enter the item, colour and quantity 
        item_input = input("Enter an item followed by it's colour and quantity, "
                + "enter STOP once you are done adding items to your shopping list: ")
        # We want to stop the loop once we are done entering all our item
        if item_input == "STOP":
            stop = True
        else:
            # We also want to add the list of item, colour and quantity to our shopping list.
            shopping_list.append(item_input.split(" "))
    return shopping_list


def can_i_buy(budget):
    ''' (int) -> str

    Given a budget, and based on the user's shopping list, check if the user can afford it.
    If they do, ask them if they would like to proceed with their purchase

    REQ: The budget has to be equal or greater than 0.

    Example:
    >>> can_i_buy(100)
    Enter an item followed by it's colour and quantity, enter STOP once you are done adding 
    items to your shopping list: shirt white 1
    Enter an item followed by it's colour and quantity, enter STOP once you are done adding 
    items to your shopping list: notebook black 2
    Enter an item followed by it's colour and quantity, enter STOP once you are done adding 
    items to your shopping list: STOP
    Yes, your total cost will be $50. Would you like to buy them? (Yes/No) Yes
    'Thanks for your purchase! Your change is $40'
    '''
    # Get the shopping list
    cart = shopping_list()
    # Create a variable to keep track of the cost
    cost = 0
    # We need to get each item from our shopping cart
    for item in cart:
        # Get its price
        price = get_item_price(item[0], item[1])
        # Add the price times the quantity to the cost
        cost += int(price) * int(item[2])
    # If we are under budget
    if budget >= cost:
        buy_message = "See you next time!"
        # Ask the user if they would like to proceed with the purchase
        confirmation = input("Yes, your total cost will be $" + str(cost) + ". Would you like to buy them? (Yes/No) ")
        # If they do, we need to update our database!
        if confirmation == "Yes":
            for item in cart:
                purchase_items(item[0], item[1], int(item[2]))
            # Informe the user that the purchase was completed and their change
            buy_message = "Thanks for your purchase! Your change is $" + str(budget - cost)
    # If we are not under budget, inform the user how much they are short.
    else:
        buy_message = "No, you are $" + str(cost - budget) + " short"
    return buy_message

def get_csv():
    ''' () -> NoneType

    Print the csv file in a table format.
    '''
    # Get the current data from the file
    csv_header, csv_data = read_csv()
    # Create some header separators
    separators = ["------------", "------------", "------------", "------------", "------------"]
    # Join all the lists to print 
    data_to_print = [csv_header] + [separators] + csv_data
    table = ""
    # Get every row of data
    for row in data_to_print:
        item_to_print = ""
        # For every row of data, you want to get every element
        for item in row:
            # We want to format every element so it has 12 characters
            # and add a tab at the end
            item_to_print += '{:12}'.format(item) + "\t"
        # For every row of data, we want to indicate it needs to be printed
        # in a new line
        table += item_to_print + "\n"
    # Print the table
    print(table)


#########################################################################
#########################################################################
############################# START HERE ################################
#########################################################################
#########################################################################
# Find the global code below:
# Read the data just so we can see it
csv_header, csv_data = read_csv()
# Let's print the header of our csv file, which we are keeping separate from
# our database, as it not a record.
print(csv_header)
# Now, let's print the database to see how it is set up:
# The database is a list inside a list, which means that every item of
# the database list represent a row
# Every row is also represented by a list, where the order of the elements
# is the same as the order of the database headers
print(csv_data)
