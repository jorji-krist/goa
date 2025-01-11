def filter_list(l):
    result = []
    for num in l:
        if isinstance(num, int):  
            result.append(num)  
    return result


def square_digits(num):
    return num * num
print(square_digits(5))


def square_digits(num):
    result = ''
    for digit in str(num):  
        result += f"{int(digit) * 2}"
    return int(result) 


def solution(text, ending):
    return text.endswith(ending)
 