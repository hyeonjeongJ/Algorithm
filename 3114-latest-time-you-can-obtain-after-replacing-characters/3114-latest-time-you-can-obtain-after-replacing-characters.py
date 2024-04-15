class Solution:
    def findLatestTime(self, s: str) -> str:
        new_s=""

        if s[0] == "?" and s[1] == "?":
            new_s += "11"
            
        elif s[0] == "?" and int(s[1]) < 2:
            new_s += "1"
            new_s += s[1]
        elif s[0] == "?" and int(s[1]) >= 2:
            new_s += "0"
            new_s += s[1]        
        elif s[0] == "0" and s[1] == "?":
            new_s += "09"
        elif s[0] == "1" and s[1] == "?":
            new_s += "11"
        else:
            new_s += s[0]
            new_s += s[1]
            
        new_s += ":"
        
        if s[3] == "?":
            new_s += "5"
        else:
            new_s += s[3]
            
        if s[4] == "?":
            new_s += "9"
        else:
            new_s += s[4]
        return new_s