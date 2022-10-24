function twoSum(nums: number[], target: number): number[] {
  let hash = new Map<number, number>();
  for (let i: number = 0; i < nums.length; i++) {
    let diff: number = target - nums[i];
    if (hash.get(diff) !== undefined) {
      return [hash.get(diff), i];
    }
    hash.set(nums[i], i);
  }
}

console.log(twoSum([2, 7, 11, 15], 9)); // Expected output: [0, 1]
console.log(twoSum([2, 3, 4], 6)); // Expected output: [0, 2]
