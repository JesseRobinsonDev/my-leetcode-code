def merge_sort(nums):
    # If there are is less than one element in the given num list, return either the empty list or single element
    if len(nums) < 2:
        return nums

    left_nums, right_nums = nums[:len(nums) // 2], nums[len(nums) // 2:]
    return merge_arrays(merge_sort(left_nums), merge_sort(right_nums))

def merge_arrays(arr1, arr2):    
    nums = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            nums.append(arr1[i])
            i += 1
        else:
            nums.append(arr2[j])
            j += 1
    leftovers = arr1[i:] + arr2[j:]
    return nums + leftovers

print(merge_sort([5, 2, 9, 1, 4, 3, 8, 6, 7]))