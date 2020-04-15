# coding:utf-8

class Node(object):
    """节点的定义"""

    def __init__(self, elem):
        self.elem = elem
        self.prev = None
        self.next = None


class DoubleLinkedList(object):
    """双向链表"""

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
        while curr is not None:
            count += 1
            curr = curr.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        curr = self.__head
        print(curr.elem, )
        while curr.next is not None:
            curr = curr.next
            print(curr.elem, )
        print("")

    def add(self, elem):
        """头部插入元素"""
        node = Node(elem)
        if self.is_empty():
            # 如果是空链表，将_head指向node
            self.__head = node
        else:
            # 将node的next指向_head的头节点
            node.next = self.__head
            # 将_head的头节点的prev指向node
            self.__head.prev = node
            # 将_head 指向node
            self.__head = node

    def append(self, elem):
        """尾部插入元素"""
        node = Node(elem)
        if self.is_empty():
            # 如果是空链表，将_head指向node
            self.__head = node
        else:
            # 移动到链表尾部
            curr = self.__head
            while curr.next is not None:
                curr = curr.next
            # 将尾节点cur的next指向node
            curr.next = node
            # 将node的prev指向cur
            node.prev = curr

    def search(self, elem):
        """查找元素是否存在"""
        curr = self.__head
        while curr is not None:
            if curr.elem == elem:
                return True
            curr = curr.next
        return False

    def insert(self, pos, elem):
        """在指定位置添加节点"""
        if pos <= 0:
            self.add(elem)
        elif pos > (self.length()-1):
            self.append(elem)
        else:
            node = Node(elem)
            curr = self.__head
            count = 0
            # 移动到指定位置的前一个位置
            while count < pos - 1:
                count += 1
                curr = curr.next
            # 将node的prev指向curr
            node.prev = curr
            # 将node的next指向cur的下一个节点
            node.next = curr.next
            # 将cur的下一个节点的prev指向node
            curr.next.prev = node
            # 将cur的next指向node
            curr.next = node

    def remove(self, elem):
        """删除元素"""
        if self.is_empty():
            return
        else:
            curr = self.__head
            if curr.elem == elem:
                # 如果首节点的元素即是要删除的元素
                if curr.next is None:
                    # 如果链表只有这一个节点
                    self.__head = None
                else:
                    # 将第二个节点的prev设置为None
                    curr.next.prev = None
                    # 将_head指向第二个节点
                    self.__head = curr.next
                return
            while curr is not None:
                if curr.elem == elem:
                    # 将cur的前一个节点的next指向cur的后一个节点
                    curr.prev.next = curr.next
                    # 将cur的后一个节点的prev指向cur的前一个节点
                    curr.next.prev = curr.prev
                    break
                curr = curr.next


if __name__ == '__main__':
    dll = DoubleLinkedList()
    dll.add(1)
    dll.add(2)
    dll.append(3)
    dll.insert(2, 4)
    # dll.insert(4, 5)
    dll.insert(0, 6)
    print("length:", dll.length())
    dll.travel()
    print(dll.search(3))
    print(dll.search(4))
    dll.remove(1)
    print("length:", dll.length())
    dll.travel()
