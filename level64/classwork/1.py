class cat:
  kitty = "cat"

p1 = cat()
print(p1.kitty)


class Jorji:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.surname}, {self.age}"

p1 = Jorji("giorgi", "qristesiashvili", 15)

print(p1)

class Person:
  def __init__(self, name, surname, age):
    self.name = name
    self.surname = surname
    self.age = age

p1 = Person("giorgi", "qristesiashvili", 15)

print(p1)
class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"{self.name} {self.surname}, Age: {self.age}"

    def name(self):
        return f"{self.name}"

    def surname(self):
        return f"{self.surname}"

    def age(self):
        return f"{self.age}"
    
person1 = Human("giorgi", "qristesiashvili", 15)