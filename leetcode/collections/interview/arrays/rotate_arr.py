from collections import deque
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        slice1 = nums[:len(nums) - k]
        slice2 = nums[-1:-1-k:-1]

        step1 = 0
        step2 = -1

        for i in range(len(nums)):
            if i < k:
                nums[i] = slice2[step2]
                step2 -= 1
            else:
                nums[i] = slice1[step1]
                step1 += 1
        print(nums)

if __name__ == '__main__':
    Solution().rotate([1, 2], 3)