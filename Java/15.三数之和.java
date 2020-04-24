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
1. 特判，对于数组长度 nn，如果数组为 nullnull 或者数组长度小于 33，返回 [][]。
2. 对数组进行排序。
3. 遍历排序后数组：
    若 nums[i]>0nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 00，直接返回结果。
    对于重复元素：跳过，避免出现重复解
    令左指针 L=i+1L=i+1，右指针 R=n-1R=n−1，当 L<RL<R 时，执行循环：
    当 nums[i]+nums[L]+nums[R]==0nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,RL,R 移到下一位置，寻找新的解
    若和大于 00，说明 nums[R]nums[R] 太大，RR 左移
    若和小于 00，说明 nums[L]nums[L] 太小，LL 右移
 */

// @lc code=start
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new LinkedList<>();
        if (nums == null || nums.length < 3) {
            return res;
        }
        Arrays.sort(nums);
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
