''' structure of linked list Node
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def addOne(self,head):
        # code here
        temp = head
        total_length = 0
        nine = 0
        while temp:
            total_length += 1
            if temp.data == 9:
                nine += 1
            else:
                nine = 0
            temp = temp.next
        if nine == total_length:
            temp = head
            while temp:
                temp.data = 0
                temp = temp.next
            one = Node(1)
            one.next = head
            head = one
        elif nine == 0:
            temp = head
            while temp.next:
                temp = temp.next
            temp.data += 1
        else:
            temp = head
            prev = None
            for _ in range(total_length - nine):
                prev = temp
                temp = temp.next
            prev.data += 1
            while temp:
                temp.data = 0
                temp = temp.next
        return head