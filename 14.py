"""Complete the script so that it removes duplicate items from the list a .

a = ["1", 1, "1", 2]
Expected output: 

  ['1', 2, 1] """


a = ["1", 1, "1", 2]
print(list(set(a)))