def positive_sum(arr):
    total = 0
    for num in arr:
        if num > 0:
            total += num
    return total

def square_sum(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total

def sum_array(a):
  return sum(a)

def find_average(array):
    return sum(array) / len(array) if array else 0

def find_average(array):
    if len(array) != 0:
        return sum(array) / len(array)
    else:
        return 0
    
def count_positives_sum_negatives(arr):
    if not arr:
        return []
    
    positive = 0
    negative = 0
    
    for num in arr:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += num
    
    return [positive, negative]