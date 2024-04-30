class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        upper = set()
        lower = set()
        
        for c in word:
            if c.isupper():
                upper.add(c.lower())
            else:
                lower.add(c.lower())
        return len(upper & lower)