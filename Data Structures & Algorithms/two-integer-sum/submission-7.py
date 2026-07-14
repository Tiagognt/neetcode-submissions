class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for index, element in enumerate(nums):
            indices[element] = index

        for index, element in enumerate(nums):
            diff = target - element
            if diff in indices and indices[diff] != index:
                return sorted([index, indices[diff]])
        return []