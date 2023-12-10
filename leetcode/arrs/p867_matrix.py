from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                new_matrix[y][x] = matrix[x][y]

        return new_matrix


if __name__ == '__main__':
    print(Solution().transpose([[1,2,3],[4,5,6]]))