"""
328. Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. Please node here we are talking
about the node number not the value in the nodes.

You should try do it in place, The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
    Given: 1 -> 2 _> 3 -> 4 -> 5 -> NULL
    return: 1 -> 3 -> 5 -> 2 -> 4 -> NULL

Note:
    The related order inside both the even and odd groups should remains as it was in the input.
    The first node is considered odd, the second node even and so on...
"""

class Solution(object):
    def odd_even_list(self, head):
        if not head or not head.next:
            return head

        cur = head
        evenhead = head.next
        evencur = head.next
        while cur.next and evencur.next:
            cur.next = evencur.next
            cur = cur.next
            evencur.next = cur.next
            evencur = evencur.next
        cur.next = evenhead

        return head

