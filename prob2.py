# Project Euler problem 2 - Even Fibonacci Numbers

# First Soltuion

def first(n1, n2, res):
    if n2 < 4000000:
        if (n1 + n2) % 2 == 0:
            res += (n1 + n2)
        first(n2, n1+n2, res)    
    else:
        print(res)


first(0, 1, 0)
