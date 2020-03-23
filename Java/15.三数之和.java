import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

/*
 * @lc app=leetcode.cn id=15 lang=java
 *
 * [15] 三数之和
 *
 * https://leetcode-cn.com/problems/3sum/description/
 *
 * algorithms
 * Medium (25.76%)
 * Likes:    1904
 * Dislikes: 0
 * Total Accepted:    176.6K
 * Total Submissions: 679K
 * Testcase Example:  '[-1,0,1,2,-1,-4]'
 *
 * 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
 * ？请你找出所有满足条件且不重复的三元组。
 * 
 * 注意：答案中不可以包含重复的三元组。
 * 
 * 
 * 
 * 示例：
 * 
 * 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
 * 
 * 满足要求的三元组集合为：
 * [
 * ⁠ [-1, 0, 1],
 * ⁠ [-1, -1, 2]
 * ]
 * 
 * 
 */

// @lc code=start
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new LinkedList<>();
        // 设置K
        for (int k = 0; k < nums.length - 2; k++) {
            if (nums[k] > 0)
                break;
            if (k == 0 || (k > 0 && nums[k] != nums[k - 1])) {
                int lo = k + 1, hi = nums.length - 1, sum = 0 - nums[k];
                while (lo < hi) {
                    // 1. 相等
                    if (nums[lo] + nums[hi] == sum) {
                        res.add(Arrays.asList(nums[k], nums[lo], nums[hi]));
                        while (lo < hi && nums[lo] == nums[lo + 1]) // 去重
                            lo++;
                        while (lo < hi && nums[hi] == nums[hi - 1]) // 去重
                            hi--;
                        lo++;
                        hi--;
                    } else if (nums[lo] + nums[hi] < sum)
                        lo++;
                    else
                        hi--;
                }
            }
        }
        return res;
    }
}
// @lc code=end
