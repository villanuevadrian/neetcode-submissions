class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            for l in s:
                if s.count(l) != t.count(l):
                    return False
        else:
            for l in t:
                if s.count(l) != t.count(l):
                    return False
        return True
            