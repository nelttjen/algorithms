class Solution:
    def reverse(self, x: int) -> int:
        new_int = 0

        mul = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            new_int *= 10
            new_int += x % 10
            x //= 10

        if not -2**31 <= (ret := new_int * mul) <= 2**31 - 1:
            return 0

        return ret


if __name__ == '__main__':
    print(Solution().reverse(00000))