def manual_difference(set1, set2):
    result = {}
    for i in set1:
        if i not in set2:
            result.append(i)
    return result

dict1 = {
    "name": "luka",
    "surname": "lomidze",
    "age": 14,
    "avg_grade": 8
}
dict2 = {
    "name": "giorgi",
    "surname": "qristesiashvili",
    "age": 10,
    "avg_grade": 10
}

both = dict1,dict2.items()

print(both)