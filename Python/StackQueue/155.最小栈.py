#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.helper = []

    # 辅助栈和数据栈不同步
    # 关键 1：辅助栈的元素空的时候，必须放入新进来的数
    # 关键 2：新来的数小于或者等于辅助栈栈顶元素的时候，才放入（特别注意这里等于要考虑进去）
    # 关键 3：出栈的时候，辅助栈的栈顶元素等于数据栈的栈顶元素，才出栈，即"出栈保持同步"就可以了

    def push(self, x: int) -> None:
        self.data.append(x)
        # 关键 1 和关键 2
        if not self.helper or self.helper[-1] >= x:
            self.helper.append(x)


    def pop(self) -> None:
        # 关键 3：【注意】不论怎么样，数据栈都要 pop 出元素
        top = self.data.pop()
        if self.helper and top == self.helper[-1]:
            self.helper.pop()


    def top(self) -> int:
        if self.data:
            return self.data[-1]


    def getMin(self) -> int:
        if self.helper:
            return self.helper[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

