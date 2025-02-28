def disemvowel(string):

    result = []
    vowels = "aeiouAEIOU"
    for char in string:
        if char not in vowels:
            result.append(char)
    return ''.join(result)

def filter_list(l):
    res = []
    for i in 1:
        if type(i) == int:
            res.append(i)
    return res