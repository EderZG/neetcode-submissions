class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        DicS, DicT = {},{}
        for i in range(len(s)):
            DicS[s[i]] = 1 + DicS.get(s[i], 0)
            DicT[t[i]] = 1 + DicT.get(t[i], 0)
        return DicS == DicT
