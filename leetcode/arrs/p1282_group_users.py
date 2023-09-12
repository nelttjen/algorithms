from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        return self.solution1(groupSizes)

    def solution1(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        result = []

        for i, size in enumerate(groupSizes):
            if size not in groups:
                groups[size] = []
            groups[size].append(i)

            if len(groups[size]) == size:
                result.append(groups[size])
                groups[size] = []

        return result

if __name__ == '__main__':
    print(Solution().groupThePeople([2,1,3,3,3,2]))