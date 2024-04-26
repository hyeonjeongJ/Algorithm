
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word_set = set(word)
        dic = {}
        for i, w in enumerate(word):
            if w.isupper() and (w.lower() in word):
                if w not in dic:
                    dic[w] = i
                    
        for i, w in enumerate(word):
            if w.islower() and (w.upper() in dic):
                if i > dic[w.upper()]:                    
                    dic.pop(w.upper())
        return len(dic)
