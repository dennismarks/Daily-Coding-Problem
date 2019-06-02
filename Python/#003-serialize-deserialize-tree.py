"""
Given the root to a binary tree, implement serialize(root), which serializes
the tree into a string, and deserialize(s), which deserializes the string
back into the tree.
"""

class Node: 

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return ("Node("
                + repr(self.val) + ", "
                + repr(self.left) + ", "
                + repr(self.right) + ")")


serialize = repr
deserialize = eval

if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
