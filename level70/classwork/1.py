sum_array = lambda a: sum(a)

class Person:
    def init(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def str(self):
        return f"{self.name} {self.surname}, {self.age}"

person1 = Person("გიორგი", "ქრისტესიაშვილი", 15)

num = 0
while num < 10:
    print("Goa best")
    num += 1