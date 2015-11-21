numbers_from_1_to_50 = range(1, 51)

square = lambda x: x ** 2

# TASK 4.1
squares_up_to_50 = [square(x) for x in numbers_from_1_to_50]
print(squares_up_to_50)

# TASK 4.2
squares_up_to_50 = map(square, numbers_from_1_to_50)
print(squares_up_to_50)
