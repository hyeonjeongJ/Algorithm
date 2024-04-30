class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word = set(word)
        count = 0
        for w in word:
            if w.lower() == w :
                if w.upper() in word:
                    count += 1
                    
        return count