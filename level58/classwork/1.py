def lottery(s):
    result = []
    for i in s:
        if i.isdigit():
            if i not in result: 
                result.append(i)
    if len(result) == 0:
        return "One more run!"
    return ''.join(result)