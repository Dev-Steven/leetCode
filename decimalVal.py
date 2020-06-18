# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # finding the length of the linked list
        ptr = head
        ctr = 0
        while ptr is not None:
            ctr += 1
            ptr = ptr.next
        # assigning length - 1 to exponent
        exponent = ctr - 1
        baseTen = 0
        currVal = head
        while currVal is not None:
            if currVal.val == 1:
                baseTen += currVal.val * 2 ** exponent
                print(baseTen)
            exponent -= 1
            currVal = currVal.next
        return baseTen