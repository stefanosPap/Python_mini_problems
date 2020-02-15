#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar = sorted(ar)
    current = ar[0]
    count = 0
    result = 0
    for i in range(n):
        if ar[i] is not current:
            current = ar[i]
            result += int(count/2) 
            count = 1
        elif i == n-1:
            count +=1
            result += int(count/2) 
        else:
            count += 1 
    return result 
#test
sockMerchant(10,[1,1,3,1,2,1,3,3,3,3])

