#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 12:19:56 2020

@author: Stefanos Papadam
"""
import copy


class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        
    # add item at the beginning of the list     
    def addBeginning(self, node):
        if self.isEmpty():
            self.head = node
             
        else:
            previousHead = self.head
            self.head = copy.copy(node)
            self.head.next = previousHead
            
    # add item at the end of the list 
    def addEnd(self, node):
        if self.isEmpty():
            self.head = node
        else:
            temp = self.head
            while True:
                if temp.next == None:
                     temp.next = copy.copy(node)         
                     break
                temp = temp.next
                
    # remove the first item that has value = element                
    def remove(self, element):
        if self.head.data == element:
            self.head = self.head.next
        else:
            temp = self.head
            while True:
                if temp.next.data == element:
                     temp.next = copy.copy(temp.next.next)         
                     break
                temp = temp.next
    # search for specific element            
    def search(self, element):
        temp = self.head
        index = 0
        while True:
            if temp.data == element:
               return index 
            if temp.next == None:
                return None
            index += 1
            temp = temp.next
            
    
    # check if list is empty 
    def isEmpty(self):
        if self.head == None :
            return 1
        else:
            return 0
        
    # print the status of the list    
    def status(self):
         temp = self.head
         while True:
            print(temp.data) 
            if temp.next == None:
                break
            temp = temp.next

        
l = LinkedList()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
l.addBeginning(n1)
l.addBeginning(n2)
l.addBeginning(n3)
l.addEnd(n4)
l.addEnd(n4)
l.addBeginning(n2)
l.addBeginning(n1)
l.addEnd(n2)
 
        
