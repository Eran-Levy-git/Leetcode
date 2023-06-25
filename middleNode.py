class Solution(object):
    def middleNode(self, head):
        temp = head
        while temp and temp.next:
            head = head.next
            temp = temp.next.next
        return head


"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""
