from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        content = {}
        output = []

        iterable_arrs = [nums1, nums2] if len(nums1) < len(nums2) else [nums2, nums1]

        for i in iterable_arrs[0]:
            try:
                content[i] += 1
            except KeyError:
                content[i] = 1

        while content:
            for i in iterable_arrs[1]:
                if i in content:
                    output.append(i)
                    content[i] -= 1
                    if content[i] == 0:
                        content.pop(i)
            break
        return output


if __name__ == '__main__':
    print(Solution().intersect([1, 2, 2, 1], [2, 2]))