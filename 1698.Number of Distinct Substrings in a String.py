# Time Complexity is O(n^2)
# Space Complexity is 
class TrieNode:
    def __init__(self):
        self.children = {}

def countDistinctSubstrings(s):
    # Write your code here
    root = TrieNode()
    cnt = 0
    for i in range(len(s)):
        node = root
        for j in range(i, len(s)):
            if s[j] not in node.children:
                node.children[s[j]] = TrieNode()
                cnt += 1
            node = node.children[s[j]]
    return cnt +1 