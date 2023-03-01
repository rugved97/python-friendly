class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def append_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def print_tree(self, level):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|---->' if self.parent else ''
        print(prefix + self.data)
        if self.get_level() < level:
            if not self.children:
                return
            for child in self.children:
                child.print_tree(level)

    def get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level


def build_location_tree():
    root = TreeNode('Global')
    india = TreeNode("India")

    gujarat = TreeNode("Gujarat")
    gujarat.append_child(TreeNode("Ahmedabad"))
    gujarat.append_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.append_child(TreeNode("Bangluru"))
    karnataka.append_child(TreeNode("Mysore"))

    india.append_child(gujarat)
    india.append_child(karnataka)

    usa = TreeNode("USA")

    nj = TreeNode("New Jersey")
    nj.append_child(TreeNode("Princeton"))
    nj.append_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.append_child(TreeNode("San Francisco"))
    california.append_child(TreeNode("Mountain View"))
    california.append_child(TreeNode("Palo Alto"))

    usa.append_child(nj)
    usa.append_child(california)

    root.append_child(india)
    root.append_child(usa)

    return root


if __name__ == '__main__':
    root_node = build_location_tree()

    root_node.print_tree(1)
