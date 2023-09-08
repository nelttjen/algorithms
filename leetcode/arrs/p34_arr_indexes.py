from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.solution1(nums, target)

    def solution1(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            median = (left + right) // 2
            if nums[median] == target:
                left, right = median, median
                while left >= 1:
                    if nums[left - 1] != target:
                        break
                    left -= 1
                while right < len(nums) - 1:
                    if nums[right + 1] != target:
                        break
                    right += 1
                return [left, right]
            elif nums[median] < target:
                left = median + 1
            else:
                right = median - 1

        return [-1, -1]


if __name__ == '__main__':
    res = Solution().searchRange([1, 2, 3, 3, 3, 3, 3, 3, 3], 8)
    print(res)