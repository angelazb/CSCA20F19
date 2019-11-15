# Enter the input number
number = input("Enter a number: ")
# Convert the number to int
number = int(number)
# Enter the input word
word = input("Enter word: ")
# Check if the length of the word is less than the number or not
if len(word) < number:
    result = len(word)
else:
    result = number
# Repeat len(word) times
for i in range(len(word)):
    # Multiply number len(word) times
    result = result * number
# Print the number
print(result)

# ***************************************************
# You can replace the for loop by this calculation:
# ** indicate exponents
# result = result * (number ** len(word))