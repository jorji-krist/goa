class bla:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = bla("maxi", 1)
dog2 = bla("loma", 2)
print("1st dog:", dog1.name, "-", dog1.age, "Y/O")
print("2nd dog:", dog2.name, "-", dog2.age, "Y/O")

class car:
    def drive(self):
        print("The car is driving")
    def stop(self):
        print("The cas has stopped")
carr = car()
carr.drive()
carr.stop()

class student():
    def __init__(self, name, subject, grade):
        self.name = name
        self.subject = subject
        self.grade = grade
    def introduce(self):
        print(f"my name is {self.name}, i study {self.subject} and my grade is {self.grade}")

student1 = student("giorgi", "math", 10)
student1.introduce()

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")
      
account = BankAccount()
account.deposit(100)
account.withdraw(50)
account.withdraw(100)