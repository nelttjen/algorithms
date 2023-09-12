from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: 'ListNode' = next

    def __repr__(self):
        return f'val: {self.val} next: {self.next}'


def list_to_linked_list(lst):
    dummy_head = ListNode()
    current = dummy_head

    for val in lst:
        current.next = ListNode(val)
        current = current.next

    return dummy_head.next


# Заданные списки
l1 = [2 ,4, 3]
l2 = [5,6,4]


# Конвертация списков в связанные списки
linked_list_l1 = list_to_linked_list(l1)
linked_list_l2 = list_to_linked_list(l2)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_node = ListNode(0)
        current = first_node
        temp = False

        while True:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            res = val1 + val2 + temp

            if res >= 10:
                res -= 10
                temp = True
            else:
                temp = False
            current.val = res
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            if not l1 and not l2:
                if temp:
                    current.next = ListNode(1)
                break

            current.next = ListNode(0)
            current = current.next

        return first_node


if __name__ == '__main__':
    print(Solution().addTwoNumbers(linked_list_l1, linked_list_l2))