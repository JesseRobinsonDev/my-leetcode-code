package main

import "fmt"

func main() {
	fmt.Println(insertion_sort([]int{5, 2, 9, 1, 4, 3, 8, 6, 7}))
}

func insertion_sort(nums_arr []int) []int {
	nums := nums_arr
	for i := 1; i < len(nums); i++ {
		num := nums[i]
		j := i - 1
		for j > -1 && nums[j] > num {
            nums[j + 1] = nums[j]
            j = j - 1
		}
        nums[j + 1] = num
	}
	return nums
}
