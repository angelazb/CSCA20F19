# Enter the input word
word = input("Enter word:")
# Initialize the result
result = 0
# Repeat for every letter in the word
for letter in word:
   # Check if the letter (lowercase) is a vowel
   if letter.lower() in "aeiou":
      # Add 1 to the results counter
      result += 1
# Print the result
print(result)

#########################################
# Another solution:
'''
# Enter the input word
word = input("Enter word:")
# Initialize the result
result = 0
# Create a vowels list
vowels = ["a", "e", "i", "o", "u"]
# Repeat for every letter in the word
for letter in word:
   # Check if the letter (lowercase) is in the list of vowels
   if letter.lower() in vowels:
      # Add 1 to the results counter
      result += 1
# Print the result
print(result)
'''
