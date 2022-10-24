# Bubble Sort
# Time Complexity: Best: O(n), Average: O(n^2), Worst: O(n^2)
# Space Complexity: O(1)
# Takes in an array of integers and returns an ascending sorted array of integers
# For the length of the array, iterate over every number in the array
# Compare them and move larger numbers to the right and smaller numbers to the left\
def bubble_sort(nums):

    # Initialize a copy of the given list of numbers
    nums = list(nums)

    # For the length of the array
    for _ in range(len(nums)):
        
        # Iterate over every number in the array (except the last, since there would be nothing to swap it with)
        for i in range(len(nums) - 1):

            # Test if the next number is greater than the current number
            # If it is, swap them to move the larger number to the end and the smaller number forward
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums
