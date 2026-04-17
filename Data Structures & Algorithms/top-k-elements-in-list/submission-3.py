class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cont = defaultdict(int)
        
        for i in range(len(nums)):
            cont[nums[i]] += 1

        res = []
        for i in range(0,k):
            maxNumber = max(cont, key=cont.get)
            res.append(maxNumber)
            cont.pop(maxNumber)
        return res
            
