
class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class Cricketer(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)
    
    def __lt__(self, other):
        return self.age < other.age


Sakib = Cricketer('Sakib', 38, 68, 91)
Mushfiq = Cricketer('Mushfiq', 36, 55, 82)
Mustafiz = Cricketer('Mustafiz', 27, 69, 86)
Riyad = Cricketer('Riyad', 39, 72, 9)

if Sakib<Mushfiq and Sakib<Mustafiz and Sakib<Riyad:
    print('Sakib')
elif Mushfiq<Sakib and Mushfiq<Mustafiz and Mushfiq<Riyad:
    print('Mushfiq')
elif Mustafiz<Sakib and Mustafiz<Mushfiq and Mustafiz<Riyad:
    print('Mustafiz')
else:
    print('Riyad')