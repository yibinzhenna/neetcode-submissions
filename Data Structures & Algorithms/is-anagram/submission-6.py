class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26

        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)