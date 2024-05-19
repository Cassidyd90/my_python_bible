# Raise our own errors
# Can choose what we want to see as error message
class Car:
    def __init__(self, make, model):
        self.make = make 
        self.model = model 

    def __repr__(self):
        return f"<Car {self.make} {self.model}"
    
    # Raise error because this method isn't ready yet
    def add_description(self):
        raise NotImplementedError("We can't do this yet")


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
     # car is from class Garage 
     # Car is from above class
     # Will only accept Car objects
    def add_car(self, car):
        if not isinstance(car, Car): 
            raise TypeError(f"Tried to add a {car.__class__.__name__} to the garage, but you can only add Car objects.")
        self.cars.append(car)


ford = Garage()
fiesta = Car("Ford", 'Fiesta')



"""
Try : will be first attempt
Except : is alternatives
Finally : always runs no matter what
"""

try:
    ford.add_car(fiesta)
except TypeError:
    print('You car is not a fiesta.')
except ValueError:
    print('Something weird happened...')
finally:
    print(f'The garage now has {len(ford)} cars')



"""
Example when not to use Finally
Try to convert to float, then n**2 
Except is Error
Else n ** 2 (Else Runs when no exceptions raised)
"""
def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid. Using default value 0')
        return 0.0
    else:
        n_square = n ** 2
        return n_square
