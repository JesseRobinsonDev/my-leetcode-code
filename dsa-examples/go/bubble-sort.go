package main

import "fmt"

func main() {
	fmt.Println(bubble_sort([]int{5, 2, 9, 1, 4, 3, 8, 6, 7}))
}

func bubble_sort(nums_arr []int) []int {
	nums := nums_arr
	for i := 0; i < len(nums); i++ {
		for j := 0; j < len(nums) - 1; j++ {
			if nums[j] > nums[j + 1] {
				nums[j], nums[j + 1] = nums[j + 1], nums[j]
			}
		}
	}
	return nums
}
