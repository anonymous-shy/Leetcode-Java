# coding:utf-8

class Node(object):
    """节点类"""

    # """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """树类"""

    def __init__(self):
        self.root = None

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        # 如果树是空的，则对根节点赋值
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                # 弹出队列的第一个元素
                curr = queue.pop(0)
                if curr.lchild is None:
                    curr.lchild = node
                    return
                elif curr.rchild is None:
                    curr.rchild = node
                    return
                else:
                    queue.append(curr.lchild)
                    queue.append(curr.rchild)

    def preorder(self, node):
        """递归实现先序遍历"""
        if node is None:
            return
        print(node.elem, end=" ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        """递归实现中序遍历"""
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem, end=" ")
        self.inorder(node.rchild)

    def posorder(self, node):
        """递归实现后续遍历"""
        if node is None:
            return
        self.posorder(node.lchild)
        self.posorder(node.rchild)
        print(node.elem, end=" ")

    def breadth_travel(self):
        """利用队列实现树的层次遍历"""
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while queue:
            node = queue.pop(0)
            print(node.elem, end=" ")
            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild is not None:
                queue.append(node.rchild)


if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print("\n")
    tree.preorder(tree.root)
    print("\n")
    tree.inorder(tree.root)
    print("\n")
    tree.posorder(tree.root)
