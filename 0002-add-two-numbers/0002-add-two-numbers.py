# Definition for singly-linked list.
# class ListNode:
# def __init__(self, val=0, next=None):
# self.val = val
# self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        dummy = l1

        list1 = []
        while dummy:
            list1.append(dummy.val)
            dummy = dummy.next
        n = len(list1)

        sum1 = 0
        for i in range(n - 1, -1, -1):

            sum1 = sum1 + list1[i] * (10 ** (i))

        dumm = l2

        list2 = []
        while dumm:
            list2.append(dumm.val)
            dumm = dumm.next
        n = len(list2)

        sum2 = 0
        for i in range(n - 1, -1, -1):

            sum2 = sum2 + list2[i] * (10 ** (i))

        sum3 = sum1 + sum2
        string3 = str(sum3)
        string4 = string3[::-1]
        length = len(string4)
        head = None
        current = None
        for i in range(length):
            if i < length - 1:
                new_node = ListNode(int(string4[i]), int(string4[i + 1]))
            else:
                new_node = ListNode(int(string4[i]))

            if head is None:
                head = new_node
                current = new_node
            else:
                current.next = new_node
                current = new_node
        return head
