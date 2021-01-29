#!/usr/local/bin/python3

# Reverse a doubly linked list

#!/bin/python3

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

def print_doubly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)

def reverse(head):
    if not head:
        return head
        
    node = head
    while node.next:
    	tmp = node.next
    	node.next = node.prev
    	node.prev = tmp
    	node = tmp

    tmp = node.next
    node.next = node.prev
    node.prev = tmp
    return node
