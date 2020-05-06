#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# https://leetcode-cn.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (48.00%)
# Likes:    871
# Dislikes: 0
# Total Accepted:    148K
# Total Submissions: 308.2K
# Testcase Example:  '2'
#

# @lc code=start

# 斐波拉契数求解
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if (n <= 2):
#             return n
#         f1, f2, f3 = 1, 2, 3
#         for i in range(3, n+1):
#             f3 = f1+f2
#             f1 = f2
#             f2 = f3
#         return f3

"""
标签：动态规划
本问题其实常规解法可以分成多个子问题，爬第n阶楼梯的方法数量，等于 2 部分之和

    1.爬上 n-1 阶楼梯的方法数量。因为再爬1阶就能到第n阶
    2.爬上 n-2 阶楼梯的方法数量，因为再爬2阶就能到第n阶
所以我们得到公式 dp[n] = dp[n-1] + dp[n-2]
同时需要初始化 dp[0]=1 和 dp[1]=1
时间复杂度：O(n)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        # if n < 3:
        #     return n
        dp = {}
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i−1] + dp[i-2]
        return dp[n]
# @lc code=end
