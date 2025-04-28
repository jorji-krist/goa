class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        print(f"{self.year} {self.brand} {self.model}")


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def s(self):
        return self.grade > 5


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def s2(self):
        print("Woof!")


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def s3(self):
        return self.width * self.height


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        print(f"{self.title}, Author: {self.author}, Year: {self.year}")