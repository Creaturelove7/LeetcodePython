# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n = ListNode()
        m = n
        count = 0
        while l1 or l2 or count:
          val = count
          if l1:
            val += l1.val
            l1 = l1.next
          if l2:
            val += l2.val
            l2 = l2.next
          
          count,val = divmod(val,10)
          m.next = ListNode(val)
          m = m.next
        return n.next
