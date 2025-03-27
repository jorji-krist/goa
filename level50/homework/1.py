def lovefunc(flower1, flower2):
    return (flower1 % 2 != flower2 % 2)

def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
def longest(s1, s2):
    return "".join(sorted(set(s1 + s2)))

def openOrSenior(data):
    categories = []
    for age, handicap in data:
        if age >= 55 and handicap > 7:
            categories.append("Senior")
        else:
            categories.append("Open")
    return categories

def grow(arr):
    n = 1
    for i in arr:
        n *= i
    return n

def printer_error(s):
    valid_letters = "abcdefghijklm"
    errors = 0
    for char in s:
        if char not in valid_letters:
            errors += 1
    return f"{errors}/{len(s)}"