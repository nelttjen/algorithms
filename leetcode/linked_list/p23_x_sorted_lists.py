import heapq
from typing import List, Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []

        first = ListNode(None)
        last = first

        for i, item in enumerate(lists):
            if item is None:
                continue
            heapq.heappush(q, (item.val, item))
            lists[i] = item.next

        while q:
            val, node = heapq.heappop(q)
            last.next = node
            last = last.next

            if node.next:
                heapq.heappush(q, (node.val, node.next))

        return first.next

