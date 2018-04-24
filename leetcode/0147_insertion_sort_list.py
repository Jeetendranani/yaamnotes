"""
147. Insertion Sort List

Sort a linked list using insertion sort.
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def insertion_sort_list(self, head):
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head

        curr = head
        while curr.next:
            if curr.next.val < curr.val:
                prev = dummy
                while prev.next.val < curr.next.val:
                    prev = prev.next
                tmp = curr.next
                curr.next = tmp.next
                tmp.next = pre.next
                prev.next = tmp
            else:
                curr = curr.next

        return dummy.next

