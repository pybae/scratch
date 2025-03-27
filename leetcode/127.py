from typing import List
from collections import deque

class Node:
    def __init__(self, word: str, neighbors: List['Node'] = []) -> 'Node':
        self.word = word
        self.neighbors = neighbors

    def __str__(self) -> str:
        return self.word

    def __repr__(self) -> str:
        return self.word

class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Build pattern-to-words mapping
        pattern_to_words = defaultdict(list)
        word_set = set(wordList)
        wordList.append(beginWord)
        L = len(beginWord)

        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_to_words[pattern].append(word)

        # Create nodes
        word_to_node: dict[str, Node] = {}
        for word in wordList:
            word_to_node[word] = Node(word)

        # Assign neighbors using pattern map
        for word in wordList:
            node = word_to_node[word]
            neighbors = set()
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                neighbors.update(pattern_to_words[pattern])
            neighbors.discard(word)  # Don't include self
            node.neighbors = [word_to_node[n] for n in neighbors]
        
        result = 1
        q = deque([word_to_node[beginWord]])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.word not in word_to_node:
                    continue
                del word_to_node[node.word]

                if node.word == endWord:
                    return result
                q.extend(neighbor for neighbor in node.neighbors if neighbor.word in word_to_node)

            result += 1

        return 0

    def string_distance(self, beginWord: str, endWord: str) -> int:
        return sum(beginWord[i] != endWord[i] for i in range(len(beginWord)))

