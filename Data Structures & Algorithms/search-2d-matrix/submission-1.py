class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])

        #Identify target belongs to which row
        row = -1
        top = 0
        bottom = rows - 1

        while top <= bottom:
            mid = top + (bottom - top) // 2
            if matrix[mid][0] <= target <= matrix[mid][cols-1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                top = mid + 1

        if row == -1:
            return False
        
        #Identify target inside the row
        left = 0
        right = cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                 right = mid - 1
            else:
                left = mid + 1
        
        return False



        
