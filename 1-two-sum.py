class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementIndexes = {}
        for i, n in enumerate(nums):
            complement = target - n
            if (complement in complementIndexes):
                return [i, complementIndexes[complement]]
            complementIndexes[n] = i
