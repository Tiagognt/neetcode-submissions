class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set, t_set = set(), set()
        if len(t) != len(s):
            return False
        return sorted(s) == sorted(t)