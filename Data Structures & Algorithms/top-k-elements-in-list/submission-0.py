class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cont = {}
        for num in nums:
            cont[num] = 1 + cont.get(num,0)

        arr = []
        for num, fec in cont.items():
            arr.append([fec, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
