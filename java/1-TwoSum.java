import java.util.HashMap;

class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] result = solution.twoSum(new int[]{2, 7, 4, 1}, 9);
        System.out.println(result[0] + " " + result[1]);
    }
}

class Solution {

    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hash = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (hash.containsKey(diff)) {
                return new int[] { hash.get(diff), i };
            }
            hash.put(nums[i], i);
        }
        return null;
    }
}