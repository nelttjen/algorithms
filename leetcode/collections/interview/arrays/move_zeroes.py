from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[index], nums[i] = num, nums[index]
                index += 1


if __name__ == '__main__':
    val = [1,2,0,3,12]
    Solution().moveZeroes(val)
    print(val)