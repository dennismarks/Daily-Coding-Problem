"""
Implement an autocomplete system. That is, given a query string s and
a set of all possible query strings, return all strings in the set that
have s as a prefix.

For example, given the query string de and the set of strings
[dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data
structure to speed up queries.
"""


class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.word_list = []

    def insert(self, key):
        node = self.root

        for c in list(key):
            if not node.children.get(c):
                node.children[c] = TrieNode()
            node = node.children[c]

        node.end = True

    def search(self, key):
        node = self.root
        word = ""

        for c in list(key):
            if not node.children.get(c):
                return False
            word += c
            node = node.children[c]

        self.search_helper(node, word)

        for word in self.word_list:
            print(word)

    def search_helper(self, node, word):
        if node.end:
            self.word_list.append(word)
        for key, value in node.children.items():
            self.search_helper(value, word + key)


if __name__ == '__main__':

    keys = ["dog", "deer", "deal", "de"]
    key = "de"
    trie = Trie()
    for s in keys:
        trie.insert(s)
    trie.search(key)

