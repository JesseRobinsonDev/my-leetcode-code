package main

import "fmt"

func main() {
	fmt.Println(merge_sort([]int{5, 2, 9, 1, 4, 3, 8, 6, 7}))
}

func merge_sort(nums_arr []int) []int {
	nums := nums_arr
	if len(nums) < 2 {
		return nums
	}
	return merge_array(merge_sort(nums[:len(nums) / 2]), merge_sort(nums[len(nums) / 2:]))
}

func merge_array(arr1 []int, arr2 []int) []int {
	var arr []int
	i, j := 0, 0

	for i < len(arr1) && j < len(arr2) {
		if arr1[i] < arr2[j] {
			arr = append(arr, arr1[i])
			i++
		} else {
			arr = append(arr, arr2[j])
			j++
		}
	}
	leftovers := append(arr1[i:], arr2[j:]...)

	return append(arr, leftovers...)
}