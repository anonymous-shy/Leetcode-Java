# coding:utf-8

class Node(object):
    """节点的定义"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleLinkedList(object):
    """单向循环链表"""

    def __init__(self):
        self.__head = None

    def is_empty(self):
        """单向循环链表"""
        return self.__head is None

    def length(self):
        """返回链表的长度"""
        # 如果链表为空，返回长度0
        if self.is_empty():
            return 0
        count = 1
        curr = self.__head
        while curr.next != self.__head:
            count += 1
            curr = curr.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        curr = self.__head
        print(curr.elem, )
        while curr.next != self.__head:
            curr = curr.next
            print(curr.elem, )
        print("")

    def add(self, elem):
        """头部添加节点"""
        node = Node(elem)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            # 添加的节点指向_head
            node.next = self.__head
            # 移到链表尾部，将尾部节点的next指向node
            curr = self.__head
            while curr.next != self.__head:
                curr = curr.next
            curr.next = node
            # _head指向添加node的
            self.__head = node

    def append(self, elem):
        """尾部添加节点"""
        node = Node(elem)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            # 移到链表尾部
            curr = self.__head
            while curr.next != self.__head:
                curr = curr.next
            # 将尾节点指向node
            curr.next = node
            # 将node指向头节点_head
            node.next = self.__head

    def insert(self, pos, elem):
        """在指定位置添加节点"""
        if pos <= 0:
            self.add(elem)
        elif pos > (self.length() - 1):
            self.append(elem)
        else:
            node = Node(elem)
            curr = self.__head
            count = 0
            # 移动到指定位置的前一个位置
            while count < pos - 1:
                count += 1
                curr = curr.next
            node.next = curr.next
            curr.next = node

    def remove(self, elem):
        """删除一个节点"""
        # 若链表为空，则直接返回
        if self.is_empty():
            return
        # 将cur指向头节点
        curr = self.__head
        pre = None
        # 若头节点的元素就是要查找删除的元素item
        if curr.elem == elem:
            # 如果链表不止一个节点
            if curr.next != self.__head:
                curr = curr.next
                # curr指向尾节点
                curr.next = self.__head.next
                self.__head = self.__head.next
            else:
                # 链表只有一个节点
                self.__head = None
        else:
            pre = self.__head
            # 第一个节点不是要删除的
            while curr.next != self.__head:
                # 找到了要删除的元素
                if curr.elem == elem:
                    # delete
                    pre.next = curr.next
                    return
                else:
                    pre = curr
                    curr = curr.next
            # cur 指向尾节点
            if curr.elem == elem:
                # 尾部删除
                pre.next = curr.next

    def search(self, elem):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        curr = self.__head
        if curr.elem == elem:
            return True
        while curr.next != self.__head:
            curr = curr.next
            if curr.elem == elem:
                return True
        return False


if __name__ == '__main__':
    scll = SingleCycleLinkedList()
    scll.add(1)
    scll.add(2)
    scll.append(3)
    scll.insert(2, 4)
    scll.insert(4, 5)
    scll.insert(0, 6)
    print("length:", scll.length())
    scll.travel()
    print(scll.search(3))
    print(scll.search(7))
    scll.remove(1)
    print('*' * 5)
    print("length:", scll.length())
    scll.travel()
