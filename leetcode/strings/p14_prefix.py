from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        chars = list(strs[0])
        chars_len = len(chars)
        for i in range(1, len(strs)):
            if chars_len > (this_len := len(strs[i])):
                chars = chars[:this_len]
                chars_len = len(chars)
            for index, char in enumerate(strs[i]):
                if index > chars_len - 1:
                    break
                if chars[index] == char:
                    continue
                chars = chars[:index]
                chars_len = len(chars)
        return ''.join(chars)


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower","flow","floight", "f"]))