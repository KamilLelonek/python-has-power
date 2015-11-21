import string

alphabet = string.ascii_lowercase

# Task 3.1
alphabet_list = [letter for letter in alphabet]
print(alphabet_list)

# TASK 3.2
alphabet_dict = {ord(letter): letter for letter in alphabet}
print(alphabet_dict)

# TASK 3.3
def filter_shorter_than_5(words):
    return [word for word in words if len(word) > 5]
    
print(filter_shorter_than_5(["abc", "abcdef"]))
