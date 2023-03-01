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

    # def print_tree(self):
    #     spaces = ' ' * self.get_level()
    #     print(spaces + self.data)
    #     if self.left:
    #         self.print_tree(self.left)
    #     if self.right:
    #         self.print_tree(self.right)
    #
    # def get_level(self):
    #     count = 0
    #     while self.left or self.right:
    #         count += 1
    #         self
    #     return count
    def pre_order_traversal(self):
        print(self.data)
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.data)
        if self.right:
            self.right.inorder_traversal()

    def inorder_traversal_array(self):
        elements = []
        if self.left:
            elements += self.left.inorder_traversal_array()
        elements.append(self.data)
        if self.right:
            elements += self.right.inorder_traversal_array()

        print(elements)
        return elements

    def post_traversal(self):
        if self.left:
            self.left.post_traversal()
        if self.right:
            self.right.post_traversal()
        print(self.data)

    def search(self, value):
        if self.data == value:
            return True
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False


if __name__ == '__main__':
    root_node = BinarySearchTreeNode(15)
    root_node.add_child(BinarySearchTreeNode(12))
    root_node.add_child(BinarySearchTreeNode(7))
    root_node.add_child(BinarySearchTreeNode(14))
    root_node.add_child(BinarySearchTreeNode(27))
    root_node.add_child(BinarySearchTreeNode(20))
    root_node.add_child(BinarySearchTreeNode(23))
    root_node.add_child(BinarySearchTreeNode(88))
    # root_node.pre_order_traversal()
    # root_node.inorder_traversal()
    root_node.inorder_traversal_array()

    print(root_node.search(89))

    # root_node.print_tree()
