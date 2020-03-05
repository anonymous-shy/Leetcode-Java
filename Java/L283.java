package xyz.shy.leetcode;

public class L283 {
}

class Solution {
    public static void moveZeroes(int[] nums) {
        int j = 0;
        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] != 0) {
                nums[j] = nums[i];
                if (i != j) {
                    nums[i] = 0;
                }
                j++;
            }
        }
    }

    // 双链表-简洁版
    private static void fixedCleanSolution(int[] nums) {
        for (int i = 0, j = 0; j < nums.length; j++) {
            if (nums[j] != 0) {
                int tmp = nums[j];
                nums[j] = nums[i];
                nums[i++] = tmp;
            }
        }
    }

    public static void main(String[] args) {
        int[] nums = {5, 1, 0, 3, 0, 7};
//        moveZeroes(nums);
        fixedCleanSolution(nums);
    }
}