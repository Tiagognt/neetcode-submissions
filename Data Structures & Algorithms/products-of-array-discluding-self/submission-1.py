class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            out[i] = prefix
            prefix *= nums[i]
        
        sufix = 1
        for i in range(len(nums)-1,-1,-1):
            out[i] *= sufix
            sufix *= nums[i]



        return out
                