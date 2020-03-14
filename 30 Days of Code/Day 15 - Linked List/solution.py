#!/usr/local/bin/python3

"""Task 

Complete the insert function in your editor so that it creates a new Node (pass data as the Node constructor argument) 
and inserts it at the tail of the linked list referenced by the head parameter. Once the new node is added, return the reference to the head node.

Note: If the head argument passed to the insert function is null, then the initial list is empty.
"""

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None 

class Solution: 
    
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        node = Node(data)
        if head is None:
            head = node
            return head
        
        current = head
        before = head
        while current:
            before = current
            current = current.next
        current = node
        before.next = current
        return head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);     
    