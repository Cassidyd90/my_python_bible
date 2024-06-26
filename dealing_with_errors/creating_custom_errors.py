"""
Type errors with code and message
Using multi line comment then is callable by .__doc__
"""

class RuntimeErrorWithCode(TypeError):
    """
    Exception raised when a specific error code is needed
    """
    def __init__(self, message, code):
        super().__init__(f"Error code {code}: {message}")
        self.code = code


err = RuntimeErrorWithCode('An error happened.', 500)
print(err.__doc__)




class UncountableError(ValueError):
    def __init__(self, wrong_value): 
        super().__init__(f"Invalid value for n, {wrong_value}. n must be greater than 0.")


def count_from_zero_to_n(n):
    if n < 1:
        raise UncountableError(n)
    for x in range(0, n + 1):
        print(x)


count_from_zero_to_n(-5)
