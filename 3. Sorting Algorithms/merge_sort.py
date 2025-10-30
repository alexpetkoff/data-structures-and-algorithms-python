def merge_sort(nums):
    nums_length = len(nums)
    
    if nums_length < 2:
        return nums

    middle_index = nums_length // 2
    
    first_list = nums[:middle_index]
    second_list = nums[middle_index:]
    
    first_res = merge_sort(first_list)
    second_res = merge_sort(second_list)

    return merge(first_res, second_res)

def merge(first, second):
    final = []
    i = 0
    j = 0

    while i < len(first) and j < len(second):        
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
            
    final.extend(first[i:])
    final.extend(second[j:])

    return final