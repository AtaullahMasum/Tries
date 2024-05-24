class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word_count = 0
        self.prefix_count = 0

class Trie:
    def __init__(self):
        
        self.root = TrieNode()
        

    def insert(self, word):
       
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1
        node.end_of_word_count += 1
        

    def countWordsEqualTo(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.end_of_word_count
            

    def countWordsStartingWith(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.prefix_count

    def erase(self, word):
       
        node = self.root
        stack = []
        for char in word:
            if char in node.children:
                stack.append((node, char))
                node = node.children[char]
            else:
                return 
        node.end_of_word_count -= 1
        # Decrease the prefix of as character and if prefix is zero then delete these node
        while stack:
            parent, char = stack.pop()
            child = parent.children[char]
            child.prefix_count -= 1
            if child.prefix_count == 0:
                del parent.children[char]
# Using List 
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end_of_word_count = 0
        self.prefix_count = 0

class Trie:
    def __init__(self):
        
        self.root = TrieNode()
        

    def insert(self, word):
       
        node = self.root
        for char in word:
            ind = ord(char) - ord('a')
            if not node.children[ind]:
                node.children[ind] = TrieNode()
            node = node.children[ind]
            node.prefix_count += 1
        node.end_of_word_count += 1
        

    def countWordsEqualTo(self, word):
        node = self.root
        for char in word:
            ind = ord(char) - ord('a')
            if not node.children[ind]:
                return 0
            node = node.children[ind]
        return node.end_of_word_count
            

    def countWordsStartingWith(self, word):
        node = self.root
        for char in word:
            ind = ord(char) - ord('a')
            if  not node.children[ind]:
                return 0
            node = node.children[ind]
        return node.prefix_count

    def erase(self, word):
       
        node = self.root
        for char in word:
            ind = ord(char) - ord('a')
            node = node.children[ind]
            node.prefix_count -= 1
        node.end_of_word_count -=1