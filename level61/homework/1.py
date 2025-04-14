def first_non_consecutive(arr):
    if len(arr) < 2:
        return None
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
    else:
        return None 

def to_alternating_case(string):
    return string.swapcase()

def correct(s):
    correct = ""
    for w in s:
        if w == '5':
            correct += 'S'
        elif w == '0':
            correct += 'O'
        elif w == '1':
            correct += 'I'
        else:
            correct += w
    return correct

def is_palindrome(s):
    s = s.lower()  
    return s == s[::-1]

def min_max(lst):
    if not lst:
        return []  
    return [min(lst), max(lst)]