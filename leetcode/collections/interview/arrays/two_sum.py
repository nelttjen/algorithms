from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solutions = dict()

        for i, num in enumerate(nums):
            search = target - num
            if search in solutions:
                return [solutions[search], i]
            solutions[num] = i
        return [0, 0]


if __name__ == '__main__':
    print(Solution().twoSum([3,2,4], 6))