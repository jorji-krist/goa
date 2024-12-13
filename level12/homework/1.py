#1
for i in (1, 50 , 2):
    print(i)

#2
fr = 5  # კვადრატის ზომა


fr = 5 
for i in range(fr):
    for j in range(fr):
        print("*", end=" ")
    print()  

print("---------------------------")

#3
width = 7 
height = 3

for i in range(height):
    for j in range(width):
        print("*", end=" ")
    print()

#4
for num1 in range(1, 4):  # გარე ციკლი
    for num in range(1, 4):  # შიდა ციკლი
        print(f"num1: {num1}, num: {num}")