def solution(str1, str2):
    return str1.endswith(str2)

def even_or_odd(s):
    even = 0
    odd = 0
    
    for i in s:
        digit = int(i)
        if digit % 2 == 0:
            even += digit  
        else:
            odd += digit 
    
    if even > odd:
        return "Even is greater than Odd"
    elif odd > even:
        return "Odd is greater than Even"
    else:
        return "Even and Odd are the same"

def even_numbers(arr,n):
    even_list = []
    for num in arr:
        if num % 2 == 0:
            even_list.append(num) 
    return even_list

def vowel_indices(word):
    word = word.lower()
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    lst = []
    for index in range(len(word)):
        if word[index] in vowels:
            lst.append(index + 1)
    return lst