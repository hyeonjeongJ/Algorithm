'''
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word = set(word)
        dic = {}
        for i, w in enumerate(word):
            if w.islower() and (w.upper() in word):
                if w not in dic:
                    dic[w] = i
                    
        for i, w in enumerate(word):
            if w.isupper() and (w.lower() in dic):
                if i < dic[w.lower()]:                    
                    dic.pop(w.lower())
        return len(dic)
'''
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        wordSet = set(word)
        dic = {}
        special = 0
        for i, char in enumerate(word):
            if char.isupper() and char.lower() in wordSet:
                if char not in dic:
                    dic[char] = i
        
        for i, char in enumerate(word):
            if char.islower() and char.upper() in dic:
                if i > dic[char.upper()]:
                    dic.pop(char.upper())
        
        return len(dic)