# Time Complexity is O(n*len) + O(n*len) = O(n*len)
# Space Complexity is O(n*len)
from sys import *
from collections import *
from math import *

from typing import *
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word_of_end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word_of_end = True
    def all_prefix_exits(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
            if not node.is_word_of_end:
                return False

        return True

def completeString(n: int, a: List[str])-> str:
    trie = Trie()
    for word in a:
        trie.insert(word)
    longest_prefix = ""
    for word in a:
        if trie.all_prefix_exits(word):
            if len(word) > len(longest_prefix):
                longest_prefix = word
            elif len(word) == len(longest_prefix) and word < longest_prefix:
                longest_prefix = word
    return longest_prefix if longest_prefix else "None"