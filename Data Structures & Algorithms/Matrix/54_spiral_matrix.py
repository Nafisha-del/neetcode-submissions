class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        output = []
        left = 0 # left pointer
        right = len(matrix[0]) # total columns
        top = 0 
        bottom = len(matrix) # total rows

        while left<right and top<bottom:
            # get every i in the top row from left to right
            for i in range(left, right):
                output.append(matrix[top][i])
            top += 1

            # get every i in the right column from top to bottom
            for i in range(top, bottom):
                output.append(matrix[i][right-1])
            right -= 1

            if not (left<right and top<bottom):
                break

            # get every i in the bottom row from right to left
            for i in range(right-1, left-1, -1):
                output.append(matrix[bottom-1][i])
            bottom -= 1

            # get every i in left column from bottom to top
            for i in range(bottom-1, top-1, -1):
                output.append(matrix[i][left])
            left += 1
        
        return output
