"""
Adding inside the function 'current' is default parameter
If you don't add name info in add_balance function, it's automatically 'current'
Default parameters always at end, can't go before amount
"""

my_account = {
    'current': 1000.25,
    'savings': 2500.50
}

def add_balance(amount: float, name: str = 'current') -> float:
    """Function to update balance of account and return the new balance."""
    my_account[name] += amount 
    return my_account[name]


print(my_account)


add_balance(500, 'savings')

print(my_account)

add_balance(650)

print(my_account)

