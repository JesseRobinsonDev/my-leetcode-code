/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  s = s.replace(/[^a-z0-9]/gi, "").toLowerCase();

  l = 0;
  r = s.length - 1;

  while (l < r) {
    if (s[l] !== s[r]) {
      return false;
    }
    l++;
    r--;
  }
  return true;
};

console.log(isPalindrome("A man, a plan, a canal: Panama")); // Expected output: True
console.log(isPalindrome("race a car")); // Expected output: False
console.log(isPalindrome(" ")); // Expected output: True
console.log(isPalindrome("joisdfjisdgji")); // Expected output: False
