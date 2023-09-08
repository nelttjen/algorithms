import random
from collections import deque

# [-5, -3, 1, 2, 3, 6]
# [1, 4, 9, 9, 25, 36]


# [-9, -3, -2, -1, 1, 2, 5, 6, 7, 10, 12]
# [1, 1, 4, 4, 9, 25, 36, 49, 81, 100, 144]
def solution_1(nums: list[int]) -> list[int]:
    result = []

    left_index, right_index = 0, len(nums) - 1

    for index, (right, left) in enumerate(zip(nums, nums[1:])):
        if right < 0 <= left:
            left_index, right_index = index, index + 1
            break

    while right_index < len(nums) and left_index >= 0:
        right_value = nums[right_index]
        left_value = abs(nums[left_index])

        if left_value < right_value:
            result.append(left_value ** 2)
            left_index -= 1
        else:
            result.append(right_value ** 2)
            right_index += 1

    while right_index < len(nums):
        result.append(nums[right_index] ** 2)
        right_index += 1

    while left_index >= 0:
        result.append(nums[left_index] ** 2)
        left_index -= 1

    return result  # 返回结果列表


# [5, 13, 14, 10, 12, 7, 6, 11, 15, 8], k = 4,
# find max in subarr len = k, ([5, 13, 14, 10] -> 14, [13, 14, 10, 12] -> 14)
# [14, 14, 14, 12, 12, 15, 15]
def solution_2(nums: list[int], k: int) -> list[int]:
    result = []
    max_deque = deque()

    for i in range(len(nums)):

        # drop all numbers that are not in our window
        while max_deque and max_deque[0] < i - k + 1:
            max_deque.popleft()

        # drop a last numbers if new is bigger than the last one in the queue
        while max_deque and nums[i] >= nums[max_deque[-1]]:
            max_deque.pop()

        # add new number to a queue
        max_deque.append(i)

        # if we're reached a point where our windows begins, start adding first number in our queue to a result
        if i >= k - 1:
            result.append(nums[max_deque[0]])

    return result


# from A to S: ['A', 'D', 'F', 'S']
# from B to S: 'no way'
graph = {'A': ['B', 'D'], 'B': ['C', 'N', 'Z'], 'D': ['E', 'F'], 'F': ['S']}


def fetch_flights(_from: str) -> list[str]:
    return graph.get(_from, [])


def find_path(_from: str, _to: str) -> list[str] | str:
    queue = deque([_from])
    # create a roadmap like to: from
    # the first element with None is the out starting point
    # when we find the last point, we can reproduce a path with asking for a previous point b key
    routes = {
        _from: None
    }

    # we need a queue to check locations where we can go from this point from the graph
    route_deque = deque()

    while queue:
        # get the oldest num in our queue
        node = queue.popleft()

        # get all available destinations
        neighs = fetch_flights(node)

        # if there's no destinations we'll skip this point
        if not neighs:
            continue

        for neigh in neighs:
            # check this destination already been processed
            if neigh not in routes:
                queue.append(neigh)

            # add a mark that we can get to this point by the point that we have checked
            routes[neigh] = node

            # we're on the destination point
            if _to == neigh:

                # add the first point to the left of the path
                route_deque.appendleft(_to)

                # set default
                parent = _to

                # while we have a destination, keep adding it to a path
                while parent:
                    # get the previous point
                    parent = routes[parent]

                    # if the previous point is None, we're in the starting point
                    if parent:

                        # otherwise add previous point to our path and continue
                        route_deque.appendleft(parent)
    # return a path if we found it to the destination point, or 'no way instead'
    return list(route_deque) or 'no way'


# arr [1..N], shuffled and 2 random numbers deleted
# find this 2 numbers
# example arr: [10, 4, 3, 9, 2, 13, 1, 14, 5, 12, 6, 8]
def find_two():
    pass


if __name__ == '__main__':
    pass


