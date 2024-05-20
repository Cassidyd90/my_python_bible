my_student = {
    "name": "Rolf Smith",
    "grades": [89, 90, 93, 78, 90],
}

def average_grade(student):
    avg = sum(student["grades"]) / len(student["grades"])

    return avg

print(average_grade(my_student))




# We've already defined a movie class like this:
class Movie:
    def __init__(self, new_name, new_director):
        self.name = new_name
        self.director = new_director

    def print_info(self):
        print(f"<<{self.name}>> by {self.director}")


movie_1 = Movie('The Matrix', 'Wachowski')
movie_2 = Movie('Goodfellas', 'Scorcese')

print(movie_1.director)

print(movie_2.print_info())


friends = ["Lilie", "Mina", "Dylan"]
print(friends.__class__)


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, i):
        return self.cars[i]
    
    def __repr__(self):
        return f"<Garage {self.cars}>"
    
    def __str__(self):
        return f"Garage with {len(self)} cars."


ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')
print(ford.cars)

print(ford[0])



# We have a class called Club, and it is initialized like this (no need to change):
class Club:
    def __init__(self, name):
        self.name = name
        self.players = []


    def __len__(self):
        return len(self.players)

    def __getitem__(self, i):
        return self.players[i]
    
    def __repr__(self):
        return f"Club {self.name}: {self.players}"
    
    
    def __str__(self):
        return f"Club {self.name} with {len(self)} players"


club_arsenal = Club("Arsenal")
club_spurs = Club("Spurs")


club_arsenal.players.append("Declan Rice")
club_arsenal.players.append("Saka")
club_arsenal.players.append("Henry")
club_spurs.players.append("Son")

print(club_arsenal.__str__())



# CLASS BEFORE INHERITANCE
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.grades = []

    def average(self):
        return sum(self.grades) / len(self.grades)
    

student_one = Student("Dylan Cassidy", "Sligo")
student_two = Student("Mina Cassidy", "Toulouse")

print(student_two.name)


# INHERITANCE
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @property  # Don't need to use the () at end of call if we add proporty
    def weekly_salary_property(self):
        return self.salary * 37.5
    
    def weekly_salary_method(self):
        return self.salary * 37.5

    
    def reverse_school_name(self):
        return str(self.school)[::-1]

rolf_worker = WorkingStudent("Rolf", 'Harvard', 17.10)

print(rolf_worker.salary)
rolf_worker.grades.append(55)
rolf_worker.grades.append(3)

print(rolf_worker.average())
print(rolf_worker.weekly_salary_property)
print(rolf_worker.weekly_salary_method())
print(rolf_worker.reverse_school_name())


# CLASSMETHOD
class Foo:
    @classmethod
    def hi(this_class):
        print(this_class.__name__)

my_object = Foo()
my_object.hi()



# STATICMETHOD (Don't use this much, it's better to use CLASSMETHOD)
class Bar:
    @staticmethod
    def hi():
        print("Hello, I don't take arguments.")

my_object_2 = Bar()
my_object_2.hi()






class FixedFloat:
    def __init__(self, amount):
        self.amount = amount 

    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>"
    
    # USING THE CLS HERE MEANS THAT IN DOLLAR IT PASSES DOLLAR AS CLASS
    # CLS IS LIKE A VARIABLE
    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)


my_float = FixedFloat(17.1567894518)
summed_numbers = FixedFloat.from_sum(19.459, 4.88256)


class Dollar(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '$'

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'


my_dollar = Dollar.from_sum(17.00, 5.00)
print(my_dollar)






