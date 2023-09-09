from functools import lru_cache
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.solution2(nums, target)

    def solution1(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = {}

        def find_combinations(remain):
            if remain in memo:
                return memo[remain]

            if remain == 0:
                return 1
            if remain < nums[0]:
                return 0

            count = 0
            for num in nums:
                if remain - num < 0:
                    break
                count += find_combinations(remain - num)
            memo[remain] = count
            return count

        return find_combinations(target)

    def solution2(self, nums, target):
        nums.sort()
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1

        for i in range(target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
                else:
                    break
        return dp[target]


if __name__ == '__main__':
    print(Solution().combinationSum4([1, 2, 4], 4))