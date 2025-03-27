def multi_table(number):
    result = ""
    for i in range(1, 11):
        result += str(i) + " * " + str(number) + " = " + str(i * number) + "\n"
    return result.strip()

def string_clean(s):
    result = ""
    for char in s:
        if not char.isdigit():
            result += char 
    return result

def between_extremes(numbers):
    return max(numbers) - min(numbers)