
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

obj = ListNode(1)
obj.next = ListNode(2)
obj.next.next = ListNode(3)
obj.next.next.next = ListNode(4)
obj.next.next.next.next = ListNode(5)

# obj.val = None
# obj = obj.next

# print each element of linked list
# print(obj.val)
# while obj.next is not None:
#     obj = obj.next
#     print(obj.val)

# why not working?>??
def removeNthFromEnd(head, n):
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next  # why head updates when this updates???
    return head

# def removeNthFromEnd(head, n):
#     dummy = ListNode(0)
#     dummy.next = head
#     fast = slow = dummy
#     for _ in range(n):
#         fast = fast.next
#     while fast and fast.next:
#         fast = fast.next
#         slow = slow.next
#     slow.next = slow.next.next
#     return dummy.next

obj2 = removeNthFromEnd(obj, 2)

print(obj2)