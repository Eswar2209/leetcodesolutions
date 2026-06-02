class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = {} 
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i + j not in d:
                    d[i + j] = []
                d[i + j].append(mat[i][j])

        arr = []
        for k in d:
            if k % 2 == 0:
                arr.extend(d[k][::-1])
            else:
                arr.extend(d[k])
        return arr