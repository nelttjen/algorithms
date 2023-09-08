class Solution:
    def generate(self, num_rows: int) -> list[list[int]]:
        return self.generate2(num_rows)

    def generate1(self, num_rows: int) -> list[list[int]]:
        results = []
        for i in range(num_rows):
            if i == 0:
                results.append([1])
                continue
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = results[i - 1][j] + results[i - 1][j - 1]

            results.append(row)
        return results

    def generate2(self, num_rows):
        pascal_triangle = []
        for line in range(1, num_rows + 1):
            current_row = [1]
            for j in range(1, line):
                print(current_row[-1], (line - j), current_row[-1] * (line - j))
                current_row.append(current_row[-1] * (line - j) // j)
            pascal_triangle.append(current_row)
        return pascal_triangle
