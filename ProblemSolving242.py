class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = tuple(sorted(s))
        sorted_t = tuple(sorted(t))
        if (sorted_s == sorted_t):
            return True
        return False