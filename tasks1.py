import string

alphabet = string.ascii_lowercase

# TASK 1.1
for letter in alphabet: print(letter)

# TASK 1.2
print(alphabet[::2])

# TASK 1.3
def is_palindrome(word):
    initial_string  = word.replace(" ", "").lower()
    reversed_string = initial_string[::-1]
    return reversed_string == initial_string

print(is_palindrome("abc"))
print(is_palindrome("A to kanapa pana Kota"))

# TASK 1.4
def filter_non_ascii(word):
    return filter(lambda letter: letter in alphabet, word)
    
print(filter_non_ascii("xyz"))
print(filter_non_ascii("ada1sd3a4"))

# TASK 1.5
def filter_longer_than_5(words):
    return filter(lambda word: len(word) > 5, words)
    
print(filter_longer_than_5(["a", "abcdef", "xyz", "xyfsdfsz"]))
