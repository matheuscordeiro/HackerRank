#!/usr/local/bin/python3

"""Task 

The height of a binary search tree is the number of edges between the tree's root and its furthest leaf. 
You are given a pointer, root, pointing to the root of a binary search tree. 
Complete the getHeight function provided in your editor so that it returns the height of the binary search tree
"""


class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        if root.left is None and root.right is None:
            return 0
        elif root.right and root.left:
            total_right = self.getHeight(root.right) + 1
            total_left = self.getHeight(root.left) + 1
            if total_right > total_left:
                return total_right
            else:
                return total_left
        elif root.right:
            return self.getHeight(root.right) + 1
        elif root.left:
            return self.getHeight(root.left) + 1

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       

