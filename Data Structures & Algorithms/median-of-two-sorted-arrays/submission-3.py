class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        A = nums1
        B = nums2
        if len(nums2) < len(nums1):
            A, B = B, A
        
        # A is smaller
        i, j = 0, len(A) - 1

        while True:
            ma = (i + j) // 2
            mb = half - ma - 2

            aleft = A[ma] if ma >= 0 else float('-inf')
            aright = A[ma + 1] if (ma + 1) < len(A) else float('inf')
            bleft = B[mb] if mb >= 0 else float('-inf')
            bright = B[mb + 1] if (mb + 1) < len(B) else float('inf')

            if aleft <= bright and bleft <= aright:
                if total % 2: # odd
                    return min(aright, bright)
                else: # even
                    return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                j = ma - 1
            else: # if bleft > aright
                i = ma + 1


