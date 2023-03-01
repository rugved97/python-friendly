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

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def calculate_sum(self):
        sum = 0
        if self.left:
            sum += self.left.calculate_sum()
        sum += self.data
        if self.right:
            sum += self.right.calculate_sum()

        return sum

    # def find_max(self):
    #     if self.right is None:
    #         return self.data
    #     return self.right.find_max()
    #
    # def find_min(self):
    #     if self.left is None:
    #         return self.data
    #     return self.left.find_min()
    #
    # def calculate_sum(self):
    #     left_sum = self.left.calculate_sum() if self.left else 0
    #     right_sum = self.right.calculate_sum() if self.right else 0
    #     return self.data + left_sum + right_sum


if __name__ == '__main__':
    root_node = BinarySearchTreeNode(15)
    root_node.add_child(BinarySearchTreeNode(12))
    root_node.add_child(BinarySearchTreeNode(7))
    root_node.add_child(BinarySearchTreeNode(14))
    root_node.add_child(BinarySearchTreeNode(27))
    root_node.add_child(BinarySearchTreeNode(20))
    root_node.add_child(BinarySearchTreeNode(23))
    root_node.add_child(BinarySearchTreeNode(88))

    print(root_node.find_min())
    print(root_node.find_max())
    print(root_node.calculate_sum())
