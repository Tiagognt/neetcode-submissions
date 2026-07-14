class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}

        for index, element in enumerate(nums):
            Map[element] = index

        for index, element in enumerate(nums):
            diff = target - element
            if diff in Map and Map[diff] != index:
                return sorted([index, Map[diff]])
        return []