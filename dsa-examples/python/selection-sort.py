# Selection Sort
# Time Complexity: Best: O(n^2), Average: O(n^2), Worst: O(n^2)
# Finds the lowest number in each iteration and swaps it with the current iteration number
def selection_sort(nums):

    nums = list(nums)

    for i in range(len(nums)):

        min_index = i

        for j in range(i + 1, len(nums)):

            if nums[min_index] > nums[j]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums
