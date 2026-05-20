class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        from collections import Counter
        s_d, t_d = Counter(s), Counter(t)

        for key in s_d:
            if s_d[key]!=t_d[key]:
                return False
        return True
        