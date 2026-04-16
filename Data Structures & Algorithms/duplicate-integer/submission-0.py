class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Dup = set()    
        for i in nums:
            if i in Dup:
                return True
            Dup.add(i) 
        return False