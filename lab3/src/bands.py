"""
CSAPX Lab 3: Battle of the Bands
Given a list of bands and the number of votes they recived, find the most mediocre band (i.e. the band with the median amount of votes)

$ python3 bands.py [slow|fast] input-file

Author: RIT CS
Author: Noah Pangilinan
"""

from dataclasses import dataclass
import sys  # argv
import time  # clock
import random  # random

from typing import List  # List
import sys


@dataclass
class Band:
   name: str
   votes: int


def load_bands(filename: str)-> list:
   bands = []
   with open(filename, encoding="utf-8") as f:
      for line in f:
         x = line.split('\t')
         bands.append(Band(x[0], int(x[1])))
   return bands


def _partition(data: list[int], pivot: int) \
      -> tuple[list[int], list[int], list[int]]:
    """
    Three way partition the data into smaller, equal and greater lists,
    in relationship to the pivot
    :param data: The data to be sorted (a list)
    :param pivot: The value to partition the data on
    :return: Three list: smaller, equal and greater
    """
    less, equal, greater = [], [], []
    for element in data:
        if element.votes < pivot:
            less.append(element)
        elif element.votes > pivot:
            greater.append(element)
        else:
            equal.append(element)
    return less, equal, greater



def quick_sort(data: list[int]) -> list[int]:
    """
    Performs a quick sort and returns a newly sorted list
    :param data: The data to be sorted (a list)
    :return: A sorted list
    """
    if len(data) == 0:
        return []
    else:
        pivot = data[0]
        less, equal, greater = _partition(data, pivot.votes)
        return quick_sort(less) + equal + quick_sort(greater)







def quick_select(data: list[int], k: int) -> Band:
   """
   Performs a partition on half of the data and finds the Kth element
   :param data: The data to be parsed (a list)
   :return: A Band object
   """
   if len(data) == 0:
        return []
   else:
      pivot = data[0]
      less, equal, greater = _partition(data, pivot.votes)
      m = len(less)
      count = (len(equal))
      
      if(m <= k and k < count+m):
         return data[k]
      if(m > k and len(data) > 0):
         return(quick_select(less, k))
      elif (len(data) > 0):
         return(quick_select(greater, (k - m - count)))
      











def main() -> None:
   """
   The main function.
   :return: None
   """
   #sorttype = sys.argv[1]
   #filename = sys.argv[2]
   sorttype = "fast"
   filename = "test-100.txt"
   i = load_bands(filename)
   bandsnum = len(i)
   k = len(i)//2
   start = time.perf_counter()
   
   if (sorttype == "slow"):
      i = quick_sort(i)
      g = (i[k])
   elif(sorttype == "fast"):
      g = (quick_select(i, k))
   print("Number of bands: " + str(bandsnum))
   print("Elapsed time: " + str(time.perf_counter() - start))
   print("Most Mediocre Band: " + str(g))

   

if __name__ == '__main__':
   main()
