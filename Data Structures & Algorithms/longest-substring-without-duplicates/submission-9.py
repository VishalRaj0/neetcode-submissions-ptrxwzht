class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 1
        window = set()
        if len(s) < 2:
            return len(s)

        i = 0
        j = 0
        while j < len(s):
            if s[j] not in window:
                window.add(s[j])
                res = max(res, j - i + 1)
                j += 1
            else:
                while i < j:
                    window.remove(s[i])
                    if s[i] == s[j]:
                        i += 1
                        break
                    i += 1
        return res


