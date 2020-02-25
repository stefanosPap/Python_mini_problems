import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    
    j = len(a) - d 
    left = [0] * len(a)
    
    for i in range(d):
        left[j] = a[i]
        j += 1
    left[0:len(a)-d] = a[d:len(a)]
    return left
    
rotLeft([1,2,3,4,5,6,7],4)