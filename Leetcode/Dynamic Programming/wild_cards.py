#DP
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) - p.count('*') > len(s): return False
        matched = [False for _ in range(len(s))]
        matched.insert(0, True)
        
        for i in p:
            if i != '*':
                for j in reversed(range(len(s))):
                    matched[j+1] = matched[j] and (i == s[j] or i == '?')
                matched[0] = False
            else:
                for j in range(1, len(s)+1):
                    matched[j] = matched[j-1] or matched[j]
        return matched[-1]
    
#Recursive way
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if (s==p) or (s==""and p.count('*')==len(p)):
            return True
        if s=="" or p=="": return False
        
        if s[-1] == p[-1] or p[-1] == '?': return self.isMatch(s[:-1], p[:-1])
        elif p[-1] == '*': return self.isMatch(s, p[:-1]) or self.isMatch(s[:-1], p[:-1]) or self.isMatch(s[:-1], p)
        
        return False