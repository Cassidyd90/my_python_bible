"""
Returns the same id each time
It's the same dictionary
"""

family = {
    'Dylan': 33,
    'Lilie': 33,
    'Mina': 3
}

def age_family(family, name):
    print(id(family))
    family[name] = 0

print(id(family))

age_family(family, 'Dylan')
print(id(family))



"""
Returns 3 id because we can't change the integer
The family dictionary has not chaged
However the Dylan property with integer has changed
"""
family = {
    'Dylan': 33,
    'Lilie': 33,
    'Mina': 3
}

def age_family(family, name):
    print(id(family))
    family[name] = 0

print(id(family))
print(id(family['Dylan']))

age_family(family, 'Dylan')

print(id(family))
print(id(family['Dylan']))




