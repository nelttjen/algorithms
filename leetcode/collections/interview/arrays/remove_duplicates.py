from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return self.solution2(nums)

    def solution1(self, nums):
        if len(nums) < 2:
            return 1
        last_index = 0
        found = False
        for i, val in enumerate(nums):
            if i == 0:
                continue
            if val == nums[last_index]:
                found = True
            else:
                last_index += 1
                nums[last_index] = val
        if found:
            return last_index + 1
        return len(nums)

    def solution2(self, nums):
        nums[:] = set(nums)
        nums.sort()
        return len(nums)


if __name__ == '__main__':
    arr = [1, 2, 3]
    expected_nums = [1, 2, 3]

    k = Solution().removeDuplicates(arr)
    print(k, arr[:k])

    assert k == len(expected_nums)
    for i in range(k):
        assert arr[i] == expected_nums[i]
