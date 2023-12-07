class Solution:
    def largestOddNumber(self, num: str) -> str:
        if len(num) == 0:
            return ''

        if int(num[-1]) % 2 != 0:
            return num

        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i+1]
        return ''


if __name__ == '__main__':
    test = Solution().largestOddNumber('52230422004')
    print(test)