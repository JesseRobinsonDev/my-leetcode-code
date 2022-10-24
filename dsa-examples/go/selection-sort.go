package main

import "fmt"

func main() {
	fmt.Println(selection_sort([]int{5, 2, 9, 1, 4, 3, 8, 6, 7}))
}

func selection_sort(nums_arr []int) []int {
	nums := nums_arr
    for i := 0; i < len(nums); i++ {
        min_index := i
        for j := i + 1; j < len(nums); j++ {
            if nums[min_index] > nums[j] {
                min_index = j
			}
		}
        nums[i], nums[min_index] = nums[min_index], nums[i]
	}
	return nums
}
