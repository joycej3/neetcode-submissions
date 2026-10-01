# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 

        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #reverse
        curr = slow.next
        prev = None
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        l1 = head
        l2 = prev
        dummy = ListNode()
        while True:
            if l1 and l2:
                dummy.next = l1
                l1 = l1.next
                dummy.next.next = l2
                l2 = l2.next
                dummy = dummy.next.next
            elif l1:
                dummy.next = l1
                return
            else:
                dummy.next = l2
                return     



