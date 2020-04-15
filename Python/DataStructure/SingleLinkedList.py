# coding:utf-8

class Node(object):
    """节点的定义"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


"""
单链表的操作
is_empty() 链表是否为空
length() 链表长度
travel() 遍历整个链表
add(item) 链表头部添加元素
append(item) 链表尾部添加元素
insert(pos, item) 指定位置添加元素
remove(item) 删除节点
search(item) 查找节点是否存在
"""


class SingleLinkedList(object):
    """单链表"""

    def __init__(self):
        self.__head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        # curr初始时指向头节点
        curr = self.__head
        count = 0
        # 尾节点指向None，当未到达尾部时
        while curr is not None:
            count += 1
            # 将curr后移一个节点
            curr = curr.next
        return count

    def travel(self):
        """遍历链表"""
        curr = self.__head
        while curr is not None:
            print(curr.elem, )
            curr = curr.next
        print("")

    def add(self, elem):
        """头部添加元素"""
        # 先创建一个保存item值的节点
        node = Node(elem)
        # 将新节点的链接域next指向头节点，即__head指向的位置
        node.next = self.__head
        # 将链表的头_head指向新节点
        self.__head = node

    def append(self, elem):
        """尾部添加元素"""
        node = Node(elem)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            self.__head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            curr = self.__head
            while curr.next is not None:
                curr = curr.next
            curr.next = node

    def insert(self, pos, elem):
        """指定位置添加元素"""
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(elem)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length() - 1):
            self.append(elem)
        # 找到指定位置
        else:
            node = Node(elem)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self.__head
            while count < pos - 1:
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

    def remove(self, elem):
        """删除节点"""
        curr = self.__head
        pre = None
        while curr is not None:
            # 找到了指定元素
            if curr.elem == elem:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self.__head = curr.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = curr.next
                break
            else:
                # 继续按链表后移节点
                pre = curr
                curr = curr.next

    def search(self, elem):
        """链表查找节点是否存在，并返回True或者False"""
        curr = self.__head
        while curr is not None:
            if curr.elem == elem:
                return True
            curr = curr.next
        return False


if __name__ == '__main__':
    """测试"""
    sll = SingleLinkedList()
    sll.add(1)
    sll.add(2)
    sll.append(3)
    sll.insert(2, 4)
    print("length:", sll.length())
    sll.travel()
    print(sll.search(3))
    print(sll.search(5))
    sll.remove(1)
    print("length:", sll.length())
    sll.travel()
