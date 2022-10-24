package main

import "fmt"

func main() {
	fmt.Println(twoSum([]int{2, 1, 5, 3}, 4)); // Expected output: [1, 3]
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9)); // Expected output: [0, 1]
	fmt.Println(twoSum([]int{7, 3, 9, 6, 1, 8, 2, 4}, 5)); // Expected output: [1, 6]
	fmt.Println(twoSum([]int{3, 5, 2, 3, 4, 3}, 6)); // Expected output: [0, 3]
}

func twoSum(nums []int, target int) []int {
	hash := make(map[int]int);
	for i := 0; i < len(nums); i++ {
		diff := target - nums[i];
		if _, ok := hash[diff]; ok {
			return []int{hash[diff], i}
		}
		hash[nums[i]] = i;
	}
	return nil;
}