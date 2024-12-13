
a1 = (input("1st: "))
a2 = (input("2nd: "))
a3 = (input("3rd: "))
a4 = (input("4th: "))
a5 = "real"
a = {a1 , a2 , a3 , a4 , a5}
print(a1, a2, a3, a4, a5)

a = {a1 , a2 , a3 , a4 , a5}


num = int(input("enter any number: "))
if num < 10:
    print("real")
else:
    print("try again")

num1 = int(input("enter another number: "))
if num1 % 2 == 0:
    print("frfr")
else:
    print("not fr")

num2 = int(input("enter any1 number:"))
if num2 > 0:
    print("ur number is positive")
else:
    print("not fr")

n1 = int(input("enter 1st number: "))
n2 = int(input("enter 2nd number: "))
if n1 == n2:
    print(n1, "=", n2)
else:
    print("not equal")

nu1 = int(input("enter one number: "))
if nu1 > 100 and nu1 % 2 == 0:
    print("right!")
else:
    print("wrong")

nu2 = int(input("one number: "))
if num2 % 5 == 0:
    print("like fr..")
else:
    print("wrong 😜")

a1 = (input("1st: "))
a2 = (input("2nd: "))
a3 = (input("3rd: "))
a4 = (input("4th: "))
a5 = "real"
a = {a1 , a2 , a3 , a4 , a5}
print(a1, a2, a3, a4, a5)


a = [9, 5, 94, 711, 52, 96, 71, 8, 33, 45]
smallest = a[0]

for number in a:
    if number < smallest:
        smallest = number
        print("ყველაზე პატარა რიცხვი:", smallest)