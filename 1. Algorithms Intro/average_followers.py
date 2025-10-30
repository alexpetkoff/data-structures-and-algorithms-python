def average_followers(nums):
    if len(nums) == 0:
        return None

    avg_followers = sum(nums) / len(nums)
    return avg_followers