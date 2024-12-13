list1 = int(input("enter a num1: "))
list2 = int(input("enter a num2: "))
list3 = int(input("enter a num3: "))
list4 = int(input("enter a num4: "))
list5 = int(input("enter a num5: "))
list = [list1, list2, list3, list4, list5]
for n in list:
    if n % 3 == 0:
        print("odd")
    else:
        print("wrong")


n1 = int(input("enter a num1: "))
n2 = int(input("enter a num2: "))
n3 = int(input("enter a num3: "))
n4 = int(input("enter a num4: "))
n5 = int(input("enter a num5: "))
list = [n1, n2, n3, n4, n5]
for n in list:
    if n % 3 == 0 and n % 5 == 0:
        print("yay")
    else:
        print("wrong")

list = ["n", "a", "m", "e"]
list = ''.join(letters)
print(list)

lines = 4
width = 6

for i in range(lines):
    print(" " * i + "*" * width)

age = int(input("enter ur age: "))
for i in range(1):
    if age < 12:
        print("ur not 12yo!")  
else:
    if age > 12 or age == 12:
        print("ur older than 12y..")
