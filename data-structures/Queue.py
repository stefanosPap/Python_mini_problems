#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:13:17 2020

@author: Stefanos Papadam
"""

class Queue:
    
    # Constructor 
    def __init__(self, length):
        self.queue = []
        self.length = length 
        self.tail = -1 
        self.head = 0
    
    # enqueue method to add an item at the end of the queue     
    def enqueue(self, element):
        if self.tail == self.length - 1:
            print("Queue is full")
        else:
            self.queue.append(element)
            self.tail += 1
            
    # dequeue method to get the first item of the queue        
    def dequeue(self):
         if self.head == self.tail:
             print("Queue is empty")
         else:
             self.queue.pop(self.head)
             self.tail -= 1
    
    # extend method to extend the length of the queue, the default value is 1  
    def extend(self, space = 1):
        self.length = self.length + space
    
    
    # status method to print to show the current status of the stack         
    def status(self):
        print(f"Queue status: {self.queue}")
        print(f"Head index: {self.head}")
        print(f"Tail index: {self.tail}")
        print(f"Max length: {self.length}")
        if self.head == self.tail:
            print('Queue is Empty')
        elif self.tail == self.length - 1:
            print("Queue is full, extend the queue using extend() method if you want to push further items.")