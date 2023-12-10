# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2

        if list1 is None and list2 is None:
            return None

        first_node = ListNode()
        last_node = first_node

        while current1 or current2:
            if current1 and current2:
                if current1.val < current2.val:
                    value = current1.val
                    current1 = current1.next
                else:
                    value = current2.val
                    current2 = current2.next
            elif current1:
                value = current1.val
                current1 = current1.next
            else:
                value = current2.val
                current2 = current2.next

            last_node.val = value
            if current1 or current2:
                last_node.next = ListNode()
                last_node = last_node.next

        return first_node


if __name__ == '__main__':
    node21 = ListNode(0)
    sol = Solution()
    node = sol.mergeTwoLists(None, None)
    print(node.val)
    while node.next:
        node = node.next
        print(node.val)