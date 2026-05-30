class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        for row in matrix:
            mn = min(row)
            col = row.index(mn)

            mx = matrix[0][col]
            for i in range(len(matrix)):
                mx = max(mx, matrix[i][col])

            if mn == mx:
                ans.append(mn)

        return ans