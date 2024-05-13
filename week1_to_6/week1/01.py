import random
import time

random.seed(100)

def QSort1(arr):
  start = time.time()
  if len(arr) <= 1:
    return arr
  pivot = arr[0]