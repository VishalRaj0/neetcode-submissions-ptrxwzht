class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = defaultdict(int)
        tdict = defaultdict(int)

        for c in s:
            sdict[c] += 1
        for c in t:
            tdict[c] += 1
        
        return sdict == tdict