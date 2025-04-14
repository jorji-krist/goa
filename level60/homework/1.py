def double_char(s):
    result = ""
    for i in s:
        result += i * 2
    return result
    
def get_age(age):
    return int(age[0])

def array_plus_array(arr1,arr2):
    total = 0
    for i in arr1:
        total += i
    for i in arr2:
        total += i
    return total