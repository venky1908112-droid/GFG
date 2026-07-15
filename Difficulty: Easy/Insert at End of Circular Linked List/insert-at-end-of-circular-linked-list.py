''' Structure of linkedlist Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def insertAtEnd(self, tail, key):
        # code here
        newnode = Node(key)
        if tail:
            head = tail.next
            tail.next = newnode
            newnode.next = head
            tail = newnode
        else:
            newnode.next = newnode
            tail = newnode
        return tail