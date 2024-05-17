

# IndexError
friends = ['Rolf', 'Anne']

friends[2]
# IndexError: list index out of range (List has only 0-1)



# KeyError
movies = [
    {'name': 'The Matrix', 'score': 8, 'year': '1994'},
    {'name': 'The Matrix 2', 'score': 7, 'year': '1998'},
    {'name': 'The Matrix 3', 'score': 9, 'year': '2002'}
]

for movie in movies:
    print(movie['title'])
# KeyError: 'title' (It should be 'name')



# NameError
print(hello)
# NameError: name 'hello' is not defined (not variable called hello)



# AttributeError
my_friends = ['Rolf', 'Jose', 'Charlie']
friends_nearby = ['Jose', 'Anna']

my_friends.intersection(friends_nearby)
# AttributeError: 'list' object has no attribute 'instersection' (Needs to be 'set' to do this)





# NotImplementedError
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        raise NotImplementedError('This feature has not been implemented yet.')
# This is an error we create



# RuntimeError
# General error , hard to define.



# SyntaxError
class User
    def __init__(self, username, password):
        self.username = username
        self.password = password
# SyntaxError: expected ':' (Missing ':' are used when defining class)



# IndentationError
def add_two(x,y):
return x+y
# IndentationError: expected an indented block after function definition on line 1



# TabError
# Can happen if use 4 spaces instead of tab



# TypeError
5 + 'hello'
# TypeError: unsupported operand type(s) for +: 'int' and 'str' (Can't add these types)



# ValueError
my_num = int(20.5)
#ValueError: Invalid literal for int() with 10: '20.5' (It should be a float because of decimal)



# ImportError
# Circular imports 



# DeprecationWarning
# It still works but python wants you to do the newer version


