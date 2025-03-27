def angle(n):
    if n > 2:
        return (n - 2) * 180
    else:
        return ""

def solution(nums):
    if nums: 
        return sorted(nums)  
    else:
        return []

def in_asc_order(arr):
    if arr == sorted(arr):
        return True
    else:
        return False