class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_unival_subtrees(tree):
    """
    A unival tree (which stands for "universal value") is a tree where
    all nodes under it have the same value.

    Given the root to a binary tree, count the number of unival subtrees.

    For example, the following tree has 5 unival subtrees:

       0
      / \
     1   0
        / \
       1   0
      / \
     1   1
    """
    if not tree:
        return 0
    elif not tree.left and not tree.right:
        return 1
    else:
        if tree.val == tree.left.val == tree.right.val:
            return 1 + count_unival_subtrees(tree.left) \
                     + count_unival_subtrees(tree.right)
        else:
            return count_unival_subtrees(tree.left) \
                   + count_unival_subtrees(tree.right)


if __name__ == '__main__':
    tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    print(count_unival_subtrees(tree))
