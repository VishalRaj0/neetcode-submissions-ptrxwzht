class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l <= r:
            m = (l + r) // 2
            if matrix[m][-1] < target:
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
            else:
                i = 0
                j = len(matrix[m]) - 1
                while i <= j:
                    mid = (i + j) // 2
                    if matrix[m][mid] < target:
                        i = mid + 1
                    elif matrix[m][mid] > target:
                        j = mid - 1
                    else:
                        return True
        
                return False
        return False
