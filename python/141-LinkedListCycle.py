from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # O(n) Time complexity, O(1) Space complexity
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

        # O(n) Time and Space complexity
        nodes = set()
        curr = head
        while curr is not None:
            next = curr.next
            if curr in nodes:
                return True
            nodes.add(curr)
            curr = next
        return False
