"""Create a function that takes any string as input and returns the number of words for that string."""

def word_count(string_variable):
    count_s = string_variable.split()
    print(len(count_s))

print(word_count("I am having a very nice day."))