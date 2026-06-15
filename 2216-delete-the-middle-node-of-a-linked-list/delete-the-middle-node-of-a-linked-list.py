# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        node_count = self.count_nodes(head)
        if node_count == 1:
            head = None
            return head
        mid = node_count // 2
        
        # Delete node at mid index
        curr = head
        for _ in range(mid-1):
            curr = curr.next
        curr.next = curr.next.next
        return head


    def count_nodes(self,node):
        count=0
        current = node
        while current is not None:
            count += 1
            current = current.next
        return count