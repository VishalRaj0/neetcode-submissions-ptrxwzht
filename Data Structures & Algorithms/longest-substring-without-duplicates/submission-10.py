class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        window = set()

        i = 0
        for j in range(len(s)):
            while s[j] in window:
                window.remove(s[i])
                i += 1
            window.add(s[j])
            res = max(res, j - i + 1)
            j += 1
        return res


