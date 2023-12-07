from collections import Counter

class Solution:
    def romanToInt(self, s: str) -> int:
        items = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        result = 0

        pointer = 0
        s_len = len(s)

        while pointer < s_len:
            value = items[s[pointer]]
            if pointer + 1 <= s_len - 1:
                value2 = items[s[pointer + 1]]
                if value2 > value:
                    result += value2 - value
                    pointer += 2
                    continue

            result += value
            pointer += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt('III'))