#!/usr/local/bin/python3

# Insert a node into a Sprted Doubly Linked List

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def sortedInsert(head, data):
    new_node = DoublyLinkedListNode(data)
    if not head:
        return new_node

    node = head
    before = None
    while node != None and node.data < data:
        before = node
        node = node.next
    
    if before:
        before.next = new_node
    else:
        head = new_node
    
    new_node.next = node
    return head

