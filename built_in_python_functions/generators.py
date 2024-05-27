"""
Doesn't store info in memory, it always remembers the last value given
'yield' is sort of like return but it runs function once, then waits
We use 'next' keyword to give values of generator
"""

def hundred_numbers():
    i = 0 
    while i < 50:
        yield i
        i += 1

g = hundred_numbers()
print((next(g))) # return 0
print((next(g))) # return 1


print(list(g)) # return list. This will start from 2 because it rememebrs from lines 14,15



def prime_generator(bound):
    for n in range(2, bound):   # n starts from 2 to bound
        for x in range(2, n):   # check if there is a number x (1<x<n) that can divide n
            if n % x == 0:  # as long as we can find any such x, then n is not prime
                break
        else:   # if no such x is found after exhausting all 1<x<n
            yield n     # generate this prime