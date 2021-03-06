#!/usr/local/bin/python3

# Insert a node at a specific position in a linked list

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

def insertNodeAtPosition(head, data, position):
    pos = 0
    node = head
    before = None
    while pos != position:
        before = node
        node = node.next
        pos += 1

    new_node = SinglyLinkedListNode(data)
    if before:
        before.next = new_node
    new_node.next = node
    return head
