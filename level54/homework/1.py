def sequence_sum(begin_number, end_number, step):
    num = 0
    current = begin_number  
    while current <= end_number: 
        num += current
        current += step  
    return num

def round_to_next5(n):
    if n % 5 == 0:
        return n 
    return n + (5 - n % 5) 

def two_oldest_ages(ages):
    sort = sorted(ages)
    return [sort[-2], sort[-1]]