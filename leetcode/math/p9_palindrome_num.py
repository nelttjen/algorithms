class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x != 0 and x % 10 == 0:
            return False

        check = 0
        while x > check:
            check = check * 10 + x % 10
            x //= 10

        return x == check or x == check // 10
