class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = defaultdict(list)
        for word in strs:
            order = ''.join(sorted(word))
            arr[order].append(word)
        return list(arr.values())

         
