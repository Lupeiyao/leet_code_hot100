


class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.is_end = False        


    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True
        

    def search_prefix(self, prefix: str) -> 'Trie':
        node = self 
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                return None
            else:
                node = node.children[idx]
        return node



    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        return node is not None and node.is_end


    def startsWith(self, prefix: str) -> bool:
        node = self.search_prefix(prefix)
        return node is not None
