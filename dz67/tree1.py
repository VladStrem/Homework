class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'Node({self.value})'


class Tree:
    def __init__(self, root: Node):
        self.root = root

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node, end="--")
            self.inorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node, end="--")

    def find_parent_by_value(self, node: Node, value: str):
        if node is None or node.value == value:
            return node
        left_search = self.find_parent_by_value(node.left, value)
        right_search = self.find_parent_by_value(node.right, value)
        return left_search if left_search else right_search

    def __contains__(self, value):
        return self.find_parent_by_value(self.root, value) is not None


if __name__ == "__main__":
    tree = Tree(root=Node("A"))
    tree.root.left = Node("B")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")
    tree.root.left.left.left = Node("H")
    tree.root.left.left.right = Node("I")

    tree.root.right = Node("C")
    tree.root.right.left = Node("F")
    tree.root.right.right = Node("G")
    tree.root.right.right.left = Node("J")

    print("In-order traversal:")
    tree.inorder(tree.root)
    print()

    print("Post-order traversal:")
    tree.postorder(tree.root)
    print()

    search_result = tree.find_parent_by_value(tree.root, 'I')
    if search_result:
        print(f"Node with value 'F' found in the subtree. Node value: {search_result.value}")
    else:
        print("Node with value 'F' not found in the subtree.")

    if 'F' in tree:
        print("Value 'F' is present in the tree.")
    else:
        print("Value 'F' is not present in the tree.")
