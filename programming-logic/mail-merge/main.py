PLACEHOLDER = "[name]"
new_name_list = []

with open("./Input/Names/invited_names.txt") as names:
    list_of_names = names.readlines()
    for name in list_of_names:
        new_name_list.append(name.strip())

with open("./Input/Letters/starting_letter.txt") as letter_model:
    letter_contents = letter_model.read()
    for name in new_name_list:
        letter = letter_contents.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(letter)
