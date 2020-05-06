#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (25.76%)
# Likes:    1904
# Dislikes: 0
# Total Accepted:    176.6K
# Total Submissions: 679K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？请你找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
# 示例：
#
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
# 1. 三层循环暴力求解
# 2. 双指针求解
# 3. hashmap 求解

# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for k in range(len(nums) - 2):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            L, R = k+1, len(nums) - 1
            while L < R:
                s = nums[k] + nums[L] + nums[R]
                if s < 0:
                    L += 1
                elif s > 0:
                    R -= 1
                else:
                    res.append((nums[k], nums[L], nums[R]))
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                    L += 1
                    R -= 1
        return res
# @lc code=end
