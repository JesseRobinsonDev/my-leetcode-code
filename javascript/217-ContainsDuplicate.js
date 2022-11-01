/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  hash = {};
  for (let i = 0; i < nums.length; i++) {
    if (hash[nums[i]] !== undefined) {
      return true;
    }
    hash[nums[i]] = i;
  }
  return false;
};

console.log(containsDuplicate([1, 2, 3, 1])); // Expected output: true
console.log(containsDuplicate([1, 2, 3, 4])); // Expected output: false
console.log(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])); // Expected output: true
