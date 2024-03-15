# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        h = head
        l = []
        while h:
            l.append(h.val)
            h = h.next
        a = l[:left-1]
        b = l[left-1:right]
        c = l[right:]
        a += b[::-1] + c
        print(a)
        d = c = ListNode(0)
        for i in a:
            c.next = ListNode(i)
            c = c.next
        return d.next