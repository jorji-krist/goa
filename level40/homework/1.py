def remove_duplicate_words(input_string):
    words = input_string.split() 
    result = []  

    for word in words:
        if word not in result:  
            result.append(word)  
    
    return ' '.join(result)

def stray(arr):
    for num in arr:
        if arr.count(num) == 1:
            return num

def solution(arr):
    if arr == None:
        return []
    arr.sort()
    return arr

def capitals(word):
    result = []
    for i in range(len(word)):
        if word[i].isupper():
            result.append(i)
    return result