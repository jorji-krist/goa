name = input("enter ur name: ")
result = ""
for i in name:
    result += i + " "
print("Result:", result)

a = int(input("enter first number: "))
b = int(input("enter second number: "))
for num in range(a, b):
    if num % 2 == 0 and num % 3 == 0:
        print("correct")
else:
    print("incorrect")

a = 0

num = int(input("enter one number: "))
for num in range(-100, 100):
    if num > 0:
        print("correct")


while True:
    num = int(input("enter one number: "))
    while num < 0:
        print("done")
        break
    else:
        print("incorrect")

