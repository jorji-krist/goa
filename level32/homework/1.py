def string_to_array(string):
    return string.split(" ")

def string_to_number(s):
    return int(s)

def fake_bin(x):
    result = ""
    for i in x:
        if int(i) < 5:
            result += '0'
        else:
            result += '1'
    return result

def high_and_low(numbers):
    nums = numbers.split()
    
    highest = int(nums[0])
    lowest = int(nums[0])
    
    for num in nums:
        num = int(num) 
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num
    
    return f"{highest} {lowest}"