class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0]*n for _ in range(n)] # nxn matrix of value 0
        val = 1

        left, right = 0, n-1
        top, bottom = 0, n-1

        while left <= right:
            # fill every value in top row
            for c in range(left, right+1):
                matrix[top][c] = val
                val += 1
            top += 1

            # fill every value in right column
            for r in range(top, bottom+1):
                matrix[r][right] = val
                val += 1
            right -= 1

            # fill every value in bottom row (reverse order)
            for c in range(right, left-1, -1):
                matrix[bottom][c] = val
                val += 1
            bottom -= 1

            # fill every value in left column (reverse order)
            for r in range(bottom, top-1, -1):
                matrix[r][left] = val
                val += 1
            left += 1
        
        return matrix
