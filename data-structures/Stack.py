#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:00:59 2020

@author: Stefanos Papadam
"""


class Stack():
    
    #Constructor
    def __init__(self, length = 1):
        self.stack = []
        self.length = length
        self.top = -1
        
    # push method to add one element at the top of the stack
    def push(self, element):
        if self.top == self.length - 1:
            print('Stack Overflow')
        else:
            self.stack.append(element)
            print(f'Element {element} inserted')
            self.top += 1
            
    # pop method to remove element from the top of the stack
    def pop(self):
        if self.top == -1:
            print('Stack Underflow')
        else:
            print(f'Element {self.stack[self.top]} has removed from stack')
            self.stack.pop()
            self.top -= 1
            
    # extend method to extend the length of the stack, the default value is 1  
    def extend(self, space = 1):
            self.length = self.length + space
    
    # returns the top element
    def topValue(self):
        if self.top != -1:
            return self.stack[self.top - 1]
        else:    
            print('Stack is Empty')
        
    
    # status method to print to show the current status of the stack         
    def status(self):
        print(f"Stack status: {self.stack}")
        print(f"Top index: {self.top}")
        print(f"Max length: {self.length}")
        if self.top == -1:
            print('Stack is Empty')
        elif self.top == self.length - 1:
            print("Stack is full, extend the stack using extend() method if you want to push further items.")