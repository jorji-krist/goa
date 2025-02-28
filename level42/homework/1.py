def sum_mix(arr):
    return sum(int(x) for x in arr)

def double_char(s):
    result = ""
    for i in s:
        result += i * 2
    return result

def array_plus_array(arr1,arr2):
    total = 0
    for i in arr1:
        total += i
    for i in arr2:
        total += i
    return total
    
def reverse_words(s):
    words = s.split(' ')
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

def sum_str(a, b):
    return int(a or 0) + int(b or 0)