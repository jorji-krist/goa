def num(n1, n2, n3):
    return lambda n: (n1 + n2 + n3) / 3

x = num(3, 5, 7)
print(x(0)) 

def even_or_odd(number):
    num = lambda n: n % 2 == 0  

    if num(number) == True: 
        return 'Even'
    else:
        return 'Odd'

def positive_sum(arr):
    return sum(0 < (lambda x: x > 0, arr))

find_min_value = lambda arr: min(arr)