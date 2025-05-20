class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Tree:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children.setdefault(char, Node())
        node.is_word = True

    def next(self, node: Node, char: str) -> tuple[Node, bool]:
        """Advance to the next node if char is valid, else return None."""
        if char in node.children:
            next_node = node.children[char]
            return next_node, next_node.is_word
        return None, False