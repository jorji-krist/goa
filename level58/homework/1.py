def vowel_one(s):
    vowels = "aeiou"
    result = ''
    for i in s:
        if i.lower() in vowels:
            result += '1'
        else:
            result += '0'
    return result

def count_letters_and_digits(s):
    count = 0 
    for i in s:
        if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z') or (i >= '0' and i <= '9'):
            count += 1

    return count

def solution(text, ending):
    return text.endswith(ending)

def elimination(arr):
    seen = set()  
    
    for i in arr:
        if i in seen:  
            return i  
        seen.add(i)  
    
    return None  