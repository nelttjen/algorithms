from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def add_digit(index, digits):
            digits[index] += 1
            if digits[index] == 10:
                digits[index] = 0
                try:
                    return add_digit(index-1, digits)
                except IndexError:
                    return [1, *digits]
            return digits

        return add_digit(-1, digits)


if __name__ == '__main__':
    print(Solution().plusOne([9, 9, 9]))