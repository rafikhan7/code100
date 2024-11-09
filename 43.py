import string

with open("letter1.txt", "w") as file:
    for letter1, letter2 in zip(string.ascii_lowercase[0::2], string.ascii_letters[1::2]):
        file.write(letter1+letter2+ "\n")