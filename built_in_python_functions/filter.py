"""
Filter takes in a function or use list comprehension
Filtering returns generator
So we need to use 'next' or 'list'
Also show a way to use list comprehension instead of filter
"""

family = ['Dylan', 'Zach', 'Mina', 'Lilie']

filter_starts_with_d = filter(lambda x: x.startswith('D'), family)
print(next(filter_starts_with_d))


non_filter_way = (x for x in family if x.startswith('D'))
print(list(non_filter_way))