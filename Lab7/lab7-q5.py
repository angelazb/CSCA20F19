# Create the function dash_separator
def dash_separator(word):
    # Initialize the result string
    result = ""
    # Loop through the word and add dashes
    for letter in word:
        result = result + letter + "-"
    # Print the result, but ignore the last dash!
    print(result[:-1])

# Enter the input word
word = input("Enter word: ")
dash_separator(word)

# ******************************************************************
# You can change the for loop in dash_separator with the following:
# index = 0
# while index < len(word):
    # result = result + word[index] + "-"
    # index += 1