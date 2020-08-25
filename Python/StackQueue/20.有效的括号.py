#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if stack and c in dic.keys():
                if stack[-1] == dic[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack

    def isValid2(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')'}
        stack = []
        for c in s:
            if c in dic: stack.append(c)
            elif len(stack) != 0 and dic[stack.pop()] != c: return False 
            else: return False
        return not stack
# @lc code=end

