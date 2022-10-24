# Insertion Sort
# Time Complexity: Best: O(n), Average: O(n^2), Worst: O(n^2)
def insertion_sort(nums):
    nums = list(nums)
    for i in range(1, len(nums)):
        num = nums[i]
        j = i - 1
        while j > -1 and nums[j] > num:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = num
    return nums