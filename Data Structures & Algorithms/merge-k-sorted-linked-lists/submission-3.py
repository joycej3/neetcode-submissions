# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def divide(self, lists):
        if not lists:
            return None
        length = len (lists)
        if length == 1:
            return lists[0]
        mid = length //2
        left = self.divide(lists[:mid])
        right = self.divide(lists[mid:])
        return self.conquer(left, right)
    
    def conquer(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        else:
            curr.next = l2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.divide(lists)
        