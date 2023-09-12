class Solution:
    def fib(self, n: int) -> int:
        return self.solution1(n)

    def solution1(self, n):
        if n < 2:
            return n
        dp = [0 for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


if __name__ == '__main__':
    print(Solution().fib(10))