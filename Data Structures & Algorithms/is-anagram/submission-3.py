class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorting = ''.join(sorted(s))
        t_sorting = ''.join(sorted(t))

        return s_sorting == t_sorting