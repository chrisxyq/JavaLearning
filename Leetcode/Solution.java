
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[j] == target - nums[i]) {
                        //java打印数组的方法Arrays.toString（数组）
                    return Arrays.toString(new int[] { i, j });
                }
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }
    public static void main(String[] args) {
        Solution solution = new Solution();
        int nums[] = {2, 7, 11, 15};
        System.out.println(111);
        System.out.println(solution.twoSum(nums,9));

        // new Solution(Solution.twoSum([1,2,3],4))
    }
}




