class HELLOClass:
    x = 5


p1 = HELLOClass
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('kate', 98)
print(p1.name)
print(p1.age)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}{self.age}'


p1 = Person('kate', 98)
print(p1)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print('hello my name is ' + self.name)


p1 = Person('kate', 200)
p1.myfunc()
# del the object
# -del p1.age
# del objects
# -del p1
print(p1.age)


# creating an employee class
class Employee:
    # define the attribute
    employee_id = 0


# create objects for the employee class
employee1 = Employee()
employee2 = Employee()

# access attributes using employee 1
employee1.EmployeeID = 1001
print(f'Employee ID:{employee1.EmployeeID}')
# access attributes using employee 2
employee2.EmployeeID = 1002
print(f'Employee ID:{employee2.EmployeeID}')


class Adding:
    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def add(self):
        return self.first_num + self.second_num


number = Adding(1, 3)

print(number.add())
