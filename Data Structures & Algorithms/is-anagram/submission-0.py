class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set, t_set = set(), set()
        if len(t) != len(s):
            return False
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
        return sorted_s == sorted_t