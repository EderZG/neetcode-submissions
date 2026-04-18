class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cont = defaultdict(int)
        bucket = [[] for _ in range(len(nums) + 1)]

        for i in range(len(nums)):
            cont[nums[i]] += 1

        for key,value in cont.items():
            bucket[value].append(key)
        
        result = []

        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

        

        