#! /usr/bin/env python3
# -*- coding = utf-8 -*-


__author__ = "Yunpeng(Randy) Li"


# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    temp = llist.head
    while temp:
        print(temp.data)
        temp = temp.next
