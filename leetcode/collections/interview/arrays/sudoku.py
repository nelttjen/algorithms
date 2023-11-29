from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = {i: set() for i in range(9)}
        segments = {i: set() for i in range(3)}

        for i, row in enumerate(board):
            if i != 0 and i % 3 == 0:
                segments = {x: set() for x in range(3)}

            row_nums = set()
            for j, cell in enumerate(row):
                if cell == '.':
                    continue

                # row check
                if cell in row_nums:
                    return False
                row_nums.add(cell)

                # segment check
                segment = j // 3
                if cell in segments[segment]:
                    return False
                segments[segment].add(cell)

                # col check
                if cell in columns[j]:
                    return False
                columns[j].add(cell)

        return True

if __name__ == '__main__':
    val = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
    print(Solution().isValidSudoku(val))
