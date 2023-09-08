from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        return self.solution1(s)

    def solution1(self, s):
        pairs = {
            '{': '}',
            '[': ']',
            '(': ')',
        }
        if not s:
            return True
        if len(s) == 1:
            return False

        que = deque()
        for symbol in s:
            if symbol == s[0]:
                if symbol not in pairs:
                    return False
                que.append(symbol)
                continue
            if symbol in pairs:
                que.append(symbol)
            else:
                if not que:
                    return False
                if symbol == pairs[que[-1]]:
                    que.pop()
                else:
                    return False
        return not bool(que)


if __name__ == '__main__':
    res = Solution().isValid('(){}}{')
    print(res)