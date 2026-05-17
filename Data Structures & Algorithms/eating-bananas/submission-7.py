class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)

        i = 0
        j = res
        while i <= j:
            m = (i + j) // 2
            if m < 1:
                break

            time_spent = 0
            for p in piles:
                time_spent += math.ceil(p / m)

            if time_spent <= h:
                j = m - 1
                res = m
            else:
                i = m + 1
        
        return res