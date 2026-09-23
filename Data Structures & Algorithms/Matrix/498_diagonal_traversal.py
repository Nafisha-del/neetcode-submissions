class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            return []

        M, N = len(mat), len(mat[0])
        result = []
        row, col = 0, 0
        direction = 1

        while len(result) < M*N:
            result.append(mat[row][col])

            if direction == 1: # Moving up-right
                if col == N-1: # Hit right wall
                    row += 1
                    direction = -1
                elif row == 0: # Hit top wall
                    col += 1
                    direction = -1
                else: # No wall hit
                    row -= 1
                    col += 1

            else: # Moving down-left
                if row == M-1: # Hit bottom wall
                    col += 1
                    direction = 1
                elif col == 0: # Hit left wall
                    row += 1
                    direction = 1
                else: # No wall hit
                    row += 1
                    col -= 1
        return result
