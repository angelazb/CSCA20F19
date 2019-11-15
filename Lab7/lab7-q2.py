# Enter the input number
number = input("Enter a number: ")
# Convert the item into an integer
number = int(number)
# Create a new list
my_list = []
# Repeat until number = 0
while number > 0:
    # Add number to the list
    my_list.append(number)
    # Change number -1
    number -= 1
# Print the list
print(my_list)