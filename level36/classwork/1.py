def digitize(n):
    return [int(digit) for digit in str(n)][::-1]

def is_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    if len(str1) != len(str2):
        return False
    
    for char in str1:
        if char not in str2:
            return False
    
    return True

def get_count(s):
    vowels = "aeiou"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def filter_list(lst):
    result = [] 
    for item in lst:
        if type(item) == int:  
            result.append(item) 
    return result