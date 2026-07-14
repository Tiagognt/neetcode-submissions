class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for n in nums:
            res[n] = 1 + res.get(n,0)
        out = []
        for i in range(k):
            n = max(res,key=res.get)
            out.append(n)
            del res[n]
        return out