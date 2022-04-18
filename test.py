import os
import sys
import math

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
for i in range(len(nums)):
      print("{0:.3f}".format(math.pow(nums[i], 1/3)))