class Solution:
    def minWindow(self, s: str, t: str) -> str:
        matches = 0
        tcount = defaultdict(int)
        window = defaultdict(int)

        for c in t:
            tcount[c] += 1
        count_to_match = len(tcount)

        res = None
        reslen = float('inf')
        i = 0
        for j in range(len(s)):
            window[s[j]] += 1
            if window[s[j]] == tcount[s[j]]:
                matches += 1
                if matches >= count_to_match:
                    while matches == count_to_match:
                        if (j - i) < reslen:
                            res = [i, j]
                            reslen = j - i + 1
                        window[s[i]] -= 1
                        if window[s[i]] < tcount[s[i]]:
                            matches -= 1
                        i += 1
                        
                    print(window)
                    print(i, j, matches)
                    print(s[i: j + 1])


        
        return s[res[0] : res[1] + 1] if res else ""

        