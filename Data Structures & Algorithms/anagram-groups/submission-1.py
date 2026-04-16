class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = defaultdict(list)
        for word in strs:
            box = [0] * 26
            for l in word:
                box[ord(l) - ord ('a')] += 1
            arr[tuple(box)].append(word)
        return list(arr.values())

         
