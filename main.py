with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_temp = letter.read()
    for name in names_list:
        stripped_name = name.strip()
        new_letter = letter_temp.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/{stripped_name}_letter.txt", "w") as text_file:
             text_file.write(new_letter)
