class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def append_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def print_tree(self, type):
        if type == 'name':
            data = self.name
        elif type == 'designation':
            data = self.designation
        else:
            data = self.name + '(' + self.designation + ')'
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|---->' if self.parent else ''
        print(prefix + data)
        if not self.children:
            return
        for child in self.children:
            child.print_tree(type)

    def get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level


def build_management_tree():
    root = TreeNode('Nilpul', 'CEO')
    branch1 = TreeNode('Chinmay', 'CTO')
    branch3 = TreeNode('Vishwa', 'Infrastructure Head')
    branch4 = TreeNode('Amir', 'Application Head')

    branch3.append_child(TreeNode('Dhaval', 'Cloud Manager'))
    branch3.append_child(TreeNode('Abhijeet', 'App Manager'))
    branch1.append_child(branch3)
    branch1.append_child(branch4)

    branch2 = TreeNode('Geld', 'HR Head')
    branch2.append_child(TreeNode('Peter', 'Recruitment Manager'))
    branch2.append_child(TreeNode('Waqas', 'Policy Manager>'))

    root.append_child(branch1)
    root.append_child(branch2)

    return root


if __name__ == '__main__':
    root_node = build_management_tree()

    root_node.print_tree("name")
    root_node.print_tree("designation")
    root_node.print_tree("both")
