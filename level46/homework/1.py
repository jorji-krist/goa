def high_and_low(numbers):
    num_list = list(map(int, numbers.split()))  
    highest = num_list[0]
    lowest = num_list[0]   

    for num in num_list:   
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num

    return f"{highest} {lowest}"

def validate_pin(pin):
    if not pin.isdigit():
        return False  
    num_list = [int(i) for i in pin] 
    a = 0
    for i in num_list: 
        a += 1  

    if a == 4: 
        return True
    elif a == 6:
        return True
    else:
        return False

def odd_or_even(arr):
    a = sum(arr)
    if a % 2 == 0:  
        return "even"
    else:
        return "odd"

def solution(nums):
    if nums: 
        return sorted(nums)  
    else:
        return []