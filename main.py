# transform [-9, -3, -2, -1, 1, 2, 5, 6, 7, 10, 12]
# into [1, 1, 4, 4, 9, 25, 36, 49, 81, 100, 144]

from other.vids.vid08_09 import 解决方案_1

result = 解决方案_1([-9, -3, -2, -1, 1, 2, 5, 6, 7, 10, 12])
print(result)

assert result == [1, 1, 4, 4, 9, 25, 36, 49, 81, 100, 144]