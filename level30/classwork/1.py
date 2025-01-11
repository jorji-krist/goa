def high_and_low(n):
    nums = n.split()
    return f"{max(nums)} {min(nums)}"
print(high_and_low("1 2 3 4 5"))  