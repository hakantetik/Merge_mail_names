# extract the names from the text as a list
with open("./Input/Names/invited_names.txt") as names:
    names_list_raw = names.readlines()

# split names from \n
names_list = []
for name in names_list_raw:
    new_name = name.split()
    names_list += new_name

# replace the [name] with names to a new text file
with open("./Input/Letters/starting_letter.txt") as letter:
    letter_temp = letter.read()

# create new text files with names and write strings in newLetters to the new text files
new_letters = []
for name in names_list:
    new_letter = letter_temp.replace("[name]", name)
    new_letters.append(new_letter)
    for letter in new_letters:
        with open(f"./Output/ReadyToSend/{name}_letter.txt", "w") as text_file:
            text_file.write(f"{letter}")

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
