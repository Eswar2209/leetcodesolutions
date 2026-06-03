class Solution:
    def findDiagonalOrder(self, mat):
        d = {}

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i + j not in d:
                    d[i + j] = []

                d[i + j].append(mat[i][j])

        ans = []

        for k in range(len(d)):
            if k % 2 == 0:
                for x in range(len(d[k]) - 1, -1, -1):
                    ans.append(d[k][x])
            else:
                for x in d[k]:
                    ans.append(x)

        return ans