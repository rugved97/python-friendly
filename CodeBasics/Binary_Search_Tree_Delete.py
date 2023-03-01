class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, node):

        if node.data == self.data:
            return
        if node.data < self.data:
            if self.left:
                self.left.add_child(node)
            else:
                self.left = node
        else:
            if self.right:
                self.right.add_child(node)
            else:
                self.right = node

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.data)
        if self.right:
            self.right.inorder_traversal()

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
            else:
                print('Not Found', self.data)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
            else:
                print('Not Found', value)
        else:

            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            # print('Here', self.right.find_max())
            self.data = self.right.find_max()
            self.right = self.right.delete(self.data)
        return self

    def delete_approach_two(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
            else:
                print('Not Found', self.data)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
            else:
                print('Not Found', value)
        else:

            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            # print('Here', self.right.find_max())
            self.data = self.left.find_min()
            self.left = self.left.delete(self.data)
        return self


if __name__ == '__main__':
    root_node = BinarySearchTreeNode(15)
    root_node.add_child(BinarySearchTreeNode(12))
    root_node.add_child(BinarySearchTreeNode(7))
    root_node.add_child(BinarySearchTreeNode(14))
    root_node.add_child(BinarySearchTreeNode(27))
    root_node.add_child(BinarySearchTreeNode(20))
    root_node.add_child(BinarySearchTreeNode(23))
    root_node.add_child(BinarySearchTreeNode(88))

    root_node.inorder_traversal()
    # root_node.delete(88)
    root_node.delete(27)

    print('After Delete')
    root_node.inorder_traversal()
