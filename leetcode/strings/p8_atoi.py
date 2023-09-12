class Solution:
    def myAtoi(self, s: str) -> int:
        return self.solution1(s)

    def solution1(self, s):
        annotations = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
        }
        to_convert = []
        # multiply = []

        pointer = 1
        # multiply_pointer = 1
        count = 0
        # multiply_count = 0
        first_contact = False

        for i, char in enumerate(s):
            if char in annotations:
                first_contact = True
                to_convert.append(char)
            elif (char == '-' or char == '+') and not first_contact:
                first_contact = True
                pointer = -1 if char == '-' else 1
            elif char == ' ' and not first_contact:
                continue
            # elif char == 'e' and first_contact:
            #     for char2 in s[i+1:]:
            #         if char2 in annotations:
            #             multiply.append(char2)
            #         else:
            #             break
            #     break
            else:
                break

        for char in to_convert[::-1]:
            count += pointer * annotations[char]
            pointer *= 10

        # if multiply:
        #     for char in multiply[::-1]:
        #         multiply_count += multiply_pointer * annotations[char]
        #         multiply_pointer *= 10
        #     count *= 10 ** multiply_count

        if count > 2147483647:
            count = 2147483647
        if count < -2147483648:
            count = -2147483648

        return count


if __name__ == '__main__':
    print(Solution().myAtoi(' -115579378e25'))