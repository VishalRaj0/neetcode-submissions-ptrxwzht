class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count = [0] * 26
        window = [0] * 26
       
        for x in range(len(s1)):
            count[ord(s1[x]) - ord('a')] += 1
            window[ord(s2[x]) - ord('a')] += 1 
        
        matches = 0
        for x in range(26):
            if count[x] == window[x]:
                matches += 1
        
        i = 0
        for j in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[j]) - ord('a')
            window[index] += 1
            if window[index] == count[index]:
                matches += 1
            elif window[index] == count[index] + 1 : # using elif because in case if its already a mismatch, we dont want to do anything with it
                matches -= 1

            
            index = ord(s2[i]) - ord('a')
            window[index] -= 1
            if window[index] == count[index]:
                matches += 1
            elif window[index] == count[index] - 1 :
                matches -= 1

            i += 1
        
        return matches == 26

