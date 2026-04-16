class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        saveNums = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in saveNums:
                return [saveNums[diff],i]
            saveNums[n] = i