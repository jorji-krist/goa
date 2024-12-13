#py bliad

age = int(input("eneter your age: "))
print(age >= 18)

score = int(input("enter ur math test score: "))
print(score >= 9)
is_B = int(input("score1: "))
print(is_B >= 8 and is_B < 9)
is_C = int(input("score2: "))
print(is_C >= 7 and is_C < 8)
is_D = int(input("score3: "))
print(is_D >= 6 and is_D <7)
is_F = int(input("score3: "))
print(is_F < 6)

number1 = 10
number2 = 14
print(number1 == number2, number1 < number2, number1 > number2, number1 <= number2, number1 >= number2)

a = int(input("1st: "))
b = int(input("2nd: "))
c = int(input("3rd: "))
if a > b and a > c:
    print("true")
if b < a and b > c:
    print("true")
if c < a and c < b:
    print("true")

score = int(input("score: ")) 
is_pass = score >= 50
is_high_pass = 75 < score < 90
is_perfect = score == 100
is_failing = score < 50
print("is_pass:", is_pass)
print("is_high_pass:", is_high_pass)
print("is_perfect:", is_perfect)
print("is_failing:", is_failing)

P = True   # ან False
Q = False  # ან True

P_and_not_Q = P and not Q
not_P_and_Q = not P and Q
P_xor_Q = (P and not Q) or (not P and Q)

print(P_and_not_Q)
print(not_P_and_Q)
print(P_xor_Q)