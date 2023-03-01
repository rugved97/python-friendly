class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def append_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|---->' if self.parent else ''
        print(prefix + self.data)
        if not self.children:
            return
        for child in self.children:
            child.print_tree()

    def get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level


if __name__ == '__main__':
    root = TreeNode('Root')

    branch1 = TreeNode('Branch1')
    branch1.append_child(TreeNode('branch1-leaf-1'))
    branch1.append_child(TreeNode('branch1-leaf-2'))
    branch1.append_child(TreeNode('branch1-leaf-3'))

    branch2 = TreeNode('Branch2')
    branch2.append_child(TreeNode('branch2-leaf-1'))
    branch2.append_child(TreeNode('branch2-leaf-2'))
    branch2.append_child(TreeNode('branch2-leaf-3'))

    branch3 = TreeNode('Branch3')
    branch3.append_child(TreeNode('branch3-leaf-1'))
    branch3.append_child(TreeNode('branch3-leaf-2'))
    branch3.append_child(TreeNode('branch3-leaf-3'))

    root.append_child(branch1)
    root.append_child(branch2)
    root.append_child(branch3)

    root.print_tree()
