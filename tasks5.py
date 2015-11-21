# TASK 5.1
def fibbonacci_generator():
    f1, f2 = 0, 1
    yield f1
    yield f2
    while True:
        current = f1 + f2
        yield current
        f1 = f2
        f2 = current

def fibbonacci_numbers(n):
    fibbonacci = fibbonacci_generator()
    return [fibbonacci.next() for _ in range(n)]
    
assert fibbonacci_numbers(14) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    
# TASK 5.2
odd_fibbonaci_numbers = [n for n in fibbonacci_numbers(14) if n % 2]

assert odd_fibbonaci_numbers == [1, 1, 3, 5, 13, 21, 55, 89, 233]
