import copy
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# def removeNthFromEnd(head, n):
#     fast = slow = head
#     for _ in range(n):
#         fast = fast.next
#     if not fast:
#         return head.next
#     while fast.next:
#         fast = fast.next
#         slow = slow.next
#     slow.next = slow.next.next
#     return head

# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

# obj_copy = copy.copy(obj)
# obj_deepcopy = copy.deepcopy(obj)

# obj.val = None
# obj = obj.next

# print each element of linked list
# print(obj.val)
# while obj.next is not None:
#     obj = obj.next
#     print(obj.val)

# def removeNthFromEnd(head, n):
#     fast = head
#     slow = head
#     for _ in range(n):
#         fast = fast.next
#     if not fast:
#         return head.next
#     while fast.next:
#         fast = fast.next
#         slow = slow.next  # at end, 3->4->5
#     slow.next = slow.next.next  # why head updates when this updates???
#     return head


# prev = None
# curr = head
# head = head.next  # need to point somewhere else before reassigning curr element, or else will overwrite everything
# curr.next = prev
# prev = curr

l1 = ListNode(3)
print(hex(id(l1)))
l1.next = ListNode(2)
print(hex(id(l1.next)))
l1.next.next = ListNode(0)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = l1.next
# l2 = ListNode(1)
# l2.next = ListNode(3)
# l2.next.next = ListNode(4)


def hasCycle(head):
    m1 = head
    m2 = head
    while m2 != None and m2.next != None:
        m1 = m1.next
        m2 = m2.next.next
        if m2 == m1:
            return True
    return False

fin = hasCycle(l1)

print('obj2')