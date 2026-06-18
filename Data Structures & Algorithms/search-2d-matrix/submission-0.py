class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Brute Force
        for row in matrix:
            for elem in row:
                if elem== target:
                    return True
        return False
        