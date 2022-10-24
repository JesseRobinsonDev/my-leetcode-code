/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 **/
var twoSum = function (nums, target) {
  map = {};

  for (var i = 0; i < nums.length; i++) {
    diff = target - nums[i];
    if (map[diff] !== undefined) {
      return [map[diff], i];
    }
    map[nums[i]] = i;
  }
};

console.log(twoSum([2, 1, 5, 3], 4)); // Expected output: [1, 3]
console.log(twoSum([2, 7, 11, 15], 9)); // Expected output: [0, 1]
console.log(twoSum([7, 3, 9, 6, 1, 8, 2, 4], 5)); // Expected output: [1, 6]
console.log(twoSum([3, 5, 2, 3, 4, 3], 6)); // Expected output: [0, 3]
