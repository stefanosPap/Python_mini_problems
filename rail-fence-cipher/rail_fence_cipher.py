#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 22:53:12 2020

@author: Stefanos Papadam
"""


def encode_rail_fence_cipher(string, n):
    
                             
    bias = 2 * n            # store biases to use them later
    biases = [0] * n
    for i in range(n):      # bias in each level are 2*n-2, 2*n-4, 2*n-6 etc.
        bias -= 2
        biases[i] = bias
    initial = -1
    encode = ""
    
                            # loop for every row
    for i in range(n):
        
        bias = biases[i]    # initial bias 
        if bias == 0:       # if we are at the final level then set bias equal to the first bias  
            bias = 2 * n - 2
        pos = initial + 1   # initial position for every loop
        initial += 1        # increase initial position  
        cross_count = 0     # count the number of crosses in order to change the bias accordingly
        
        while True:
                                    # condition for breaking the loop
            if pos >= len(string):  # if position surpassed string's length then break
                break
            
            encode += string[pos]   # update encoded string 
            pos += bias             # take next position  
            cross_count += 1
            if i != 0 and i != n - 1:       # change the bias 
                if cross_count % 2 == 1:    # odd crosses
                    bias = biases[- i - 1]  # change bias with its symmetric of the array biases
                else:                       # even crosses
                    bias = biases[i]
             
    return encode                           # return encoded string 
def decode_rail_fence_cipher(string, n):
    pass


string = ""
encode = encode_rail_fence_cipher(string, 4)