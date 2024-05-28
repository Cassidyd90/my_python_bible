"""
Produces generator so need 'next' or 'list'
Similar to filter it takes a function or list comprehension
Also show ways of doing same thing without using 'map'
"""

family = ['Dylan', 'Zach', 'Mina', 'Lilie']

family_lower = map(lambda x: x.lower(), family)
print(list(family_lower))


family_lower_list_comp = [x.lower() for x in family]
print(family_lower_list_comp)

family_lower_generator = (x.lower() for x in family)
print(next(family_lower_generator))
print(next(family_lower_generator))