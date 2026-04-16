class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countT, countS = {} , {}

        for i in range(len(s)):
            countT[s[i]] = 1 + countT.get(s[i], 0)
            countS[t[i]] = 1 + countS.get(t[i], 0)

        return countT == countS
