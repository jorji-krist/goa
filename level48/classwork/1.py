def xo(s):
    a = 0
    b = 0
    for i in s:
        if i == 'x':
            a += 1
        elif i == 'o':
            b += 1
    return a == b

def find_short(s):
    words = s.split() 
    shortest_word = min(words)
    return len(shortest_word)

def solution(text, ending):
    return text.endswith(ending)