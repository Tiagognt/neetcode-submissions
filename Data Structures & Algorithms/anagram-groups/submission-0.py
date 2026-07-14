class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        out = []
        for i in range(len(strs)):
            if "".join(sorted(strs[i])) in d:
                d["".join(sorted(strs[i]))].append(strs[i])
            else:
                d["".join(sorted(strs[i]))] = [strs[i]]
        out = [d[e] for e in d]
        return out


