# Project Euler problem 1 - Multiples of 3 or 5

# First Solution
def first():
    multiples = 0
    for i in range(1,1000):
        if i % 5 == 0 or i % 3 == 0:
            multiples += i
    print(multiples)


first()
