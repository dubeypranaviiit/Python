# Get the input string and character from the user
string_input = input("Enter a string: ")
char_input = input("Enter a character: ")
count = 0
for char in string_input:
    if char == char_input:
        count += 1

print("The character '{}' appears {} times in the string.".format(char_input, count))