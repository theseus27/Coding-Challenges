#Recursive way
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if (s==p) or (s==""and p.count('*')==len(p)):
            return True
        if s=="" or p=="": return False
        
        if s[-1] == p[-1] or p[-1] == '?': return self.isMatch(s[:-1], p[:-1])
        elif p[-1] == '*': return self.isMatch(s, p[:-1]) or self.isMatch(s[:-1], p[:-1]) or self.isMatch(s[:-1], p)
        
        return False