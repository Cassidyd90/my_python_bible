"""
The 'family' variable just indicates the data
The data is stored in RAM while app running
using 'id' gives the number object which is running in RAM
The 2 dictionaries look the same but they are not the same, 2 seperate things
When changing the 2nd object, the id remains the same. 
"""

family = {
    'Dylan': 33,
    'Lilie': 33,
    'Mina': 3
}


print(id(family))

family = {
    'Dylan': 33,
    'Lilie': 33,
    'Mina': 3
}

print(id(family))

family['Dylan'] = 30

print(id(family))


"""
Integers are immutable
5 is always 5, it can never be anything else
The id will be different because 5 is not the same as 7
IMMUTABLE 
integers
floats
strings
tuples
"""

my_int = 5 

print(id(my_int))

my_int = my_int + 2

print(id(my_int))




"""
Lists are mutable
Change the list friends but id number remains the same
"""

friends = ['David', 'Daniel']
print(id(friends))

friends.append('Ciaran')
print(id(friends))



