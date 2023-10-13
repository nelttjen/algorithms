from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1

        while left <= right:
            left_num = nums[left]
            right_num = nums[right]
            if target - left_num == right_num:
                return [left+1, right]
            if target < right_num:
                right -= 1
                continue

            if target - left_num > 0:
                left += 1
                continue
            if target - right_num < 0:
                right -= 1
                continue


if __name__ == '__main__':
    print(Solution().twoSum([-1, 0], -1))