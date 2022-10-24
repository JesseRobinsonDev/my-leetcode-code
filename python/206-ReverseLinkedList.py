from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr is not None:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp

        head = prev
        return head

node5 = ListNode("5")
node4 = ListNode("4", node5)
node3 = ListNode("3", node4)
node2 = ListNode("2", node3)
node1 = ListNode("1", node2)

solution = Solution()