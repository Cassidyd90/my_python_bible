"""
'any' returns if any values evaluate to True
'all' returns true if all values are True
"""

family = [
    {
        'name': 'Dylan',
        'age': 33
    },
    {
        'name': 'Zach',
        'age': 27
    },
    {
        'name': 'Mina',
        'age': 3
    },
]


movie_age = input('What age is this movie for? ')

movie_suitability_check = [x for x in family if x['age'] > movie_age]

if any(movie_suitability_check):
    print("You're old enough to go in.")

if all(movie_suitability_check):
    print("You're old enough to go in.")
else:
    print("Not everyone can enter.")