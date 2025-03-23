from typing import Optional

class Node:

    children: list[Optional['Node']]
    is_word: bool

    def __init__(self):
        self.children = [None] * 26
        self.is_word = False

    def add_child(self, char: str, node: Optional['Node']) -> Optional['Node']:
        self.children[ord(char) - ord('a')] = node
        return node

    def get_child(self, char: str) -> Optional['Node']:
        return self.children[ord(char) - ord('a')]


class Trie:

    root: Node

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            child = current.get_child(char)
            if not child:
                child = current.add_child(char, Node())
            current = child
        current.is_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            current = current.get_child(char)
            if not current:
                return False
        return current.is_word
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            current = current.get_child(char)
            if not current:
                return False
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app");
print(trie.search("app"))
