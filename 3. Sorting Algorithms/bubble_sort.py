def bubble_sort(nums):
    sorted_list = nums
    swapping = True
    end = len(sorted_list)

    while swapping is True:
        swapping = False
        for i in range(1, end):
            if sorted_list[i-1] > sorted_list[i]:
                sorted_list[i-1], sorted_list[i] = sorted_list[i], sorted_list[i-1]
                swapping = True
        end = end - 1

    return sorted_list