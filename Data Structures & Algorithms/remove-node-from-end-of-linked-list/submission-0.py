# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        we will be solving this question by two pointer. first we will create a dummy node. from that dummy node till the value of n. that end value will be r. we will increment both the values till r is null and thats when we get out value
        """
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n>0 and right:
            right = right.next
            n-=1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next