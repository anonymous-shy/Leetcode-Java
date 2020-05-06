/*
 * @lc app=leetcode.cn id=11 lang=java
 *
 * [11] 盛最多水的容器
 */

// 1. 枚举法：left bar x,right bar y, area = (x-y)*height_diff
// O(n^2)
// class Solution {
//     public int maxArea(int[] height) {
//         int max = 0;
//         for (int i = 0; i < height.length; ++i) {
//             for (int j = i+1; j < height.length; ++j){
//                 int area = (j - i) * Math.min(height[i], height[j]);
//                 max = Math.max(max, area);
//             }
//         }
//         return max;
//     }
// }

// 2.双指针法： O(N) 左右边界 i，j 向中间收敛，左右夹逼
// @lc code=start
class Solution {
    public int maxArea(int[] height) {
        int max = 0;
        for (int i = 0, j = height.length - 1; i < j;) {
            int minHeight = height[i] < height[j] ? height[i++] : height[j--];
            int area = (j - i + 1) * minHeight;
            max = Math.max(max, area);
        }
        return max;
    }
}
// @lc code=end
