# write a program that has O(n)

def find_max(nums):
    max = float('-inf')

    for num in nums:
        if num > max:
            max = num

    return max