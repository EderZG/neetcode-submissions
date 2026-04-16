class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        val = {}

        for i,n in enumerate(nums):
            rest = target - n
            if rest in val:
                return [val[rest],i]
            val[n] = i
        return []