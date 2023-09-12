from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        deletions = 0
        used_counts = set()

        for count in cnt.values():
            while count in used_counts and count > 0:
                deletions += 1
                count -= 1
            used_counts.add(count)

        return deletions


if __name__ == '__main__':
    print(Solution().minDeletions('ceabaacb'))