/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function (height) {
  let leftMax = height[0];
  let rightMax = height[height.length - 1];
  let l = 0;
  let r = height.length - 1;
  let res = 0;

  while (l < r) {
    if (leftMax < rightMax) {
      l++;
      leftMax = Math.max(leftMax, height[l]);
      res += leftMax - height[l];
    } else {
      r--;
      rightMax = Math.max(rightMax, height[r]);
      res += rightMax - height[r];
    }
  }

  return res;
};

console.log(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])); // Expected output: 6
console.log(trap([4, 2, 0, 3, 2, 5])); // Expected output: 9
