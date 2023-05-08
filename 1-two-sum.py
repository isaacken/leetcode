class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            for j, n2 in enumerate(islice(nums, i + 1, len(nums))):
                if (n + n2) == target:
                    return [i, i+j+1]