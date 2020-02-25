import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    summary = []
    
    for i in range(1,len(arr)-1):
        for j in range(1,len(arr[0])-1):
    
            temp = arr[i][j] + arr[i-1][j] + arr[i+1][j] + arr[i-1][j-1] + arr[i-1][j+1] + arr[i+1][j-1] + arr[i+1][j+1]
            summary.append(temp)
    
    maximum = max(summary)
    return maximum

#test
arr = [
[-1,-1,0,-9,-2,-2],
[-2,-1,-6,-8,-2,-5],
[-1,-1,-1,-2,-3,-4],
[-1,-9,-2,-4,-4,-5],
[-7,-3,-3,-2,-9,-9],
[-1,-3,-1,-2,-4,-5]]


hourglassSum(arr)