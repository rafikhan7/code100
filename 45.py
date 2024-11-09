import string

for i in string.ascii_lowercase:
    print(i)
    with open(i+".txt", 'w') as file:
        file.write(i)