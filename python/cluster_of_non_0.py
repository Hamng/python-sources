# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 07:38:05 2020

@author: Ham

Self Challenge: Count Cluster of Non-0s

Given a 1-dimension array of integers,
determine how many 'clusters' of non-0 in the array.
A 'cluster' is a group of consecutive non-0 values.

Scoring: a solution needs to be a 1-liner;
i.e. NO point if implementing with a traditional 'for' loop!

Sample Input (see STDIN_SIO)

A : [
  9,  0,  0, 22,  0,  0, 39, 11,  3,  0, \
  0, 24,  1,  0, 50, 23,  3, 44,  0, 23, \
 25,  6, 36, 19, 10, 23,  0, 37,  4,  1, \
  7, 12,  0,  0, 49
 ]

Expected Output:
8

"""

import itertools


STDIN_SIO = """
  9,  0,  0, 22,  0,  0, 39, 11,  3,  0, \
  0, 24,  1,  0, 50, 23,  3, 44,  0, 23, \
  2,  8, 20, 35,  0, 40, 34, 26, 36,  0, \
 35, 19, 20, 18, 11, 43, 19, 21, 40,  0, \
 14,  0, 14,  0,  0, 25, 35, 24, 49, 15, \
 13,  3,  0, 10, 31, 25, 27, 37, 27, 43, \
 44, 27,  8, 43,  0,  0, 33, 25, 19, 47, \
  0, 29,  5,  2, 12,  8,  7,  0, 16, 36, \
  0,  6, 17, 35, 36, 21,  0,  9,  1,  0, \
 43, 29, 39, 15, 18,  0, 34, 26, 48,  0, \
 34, 35,  7, 10,  0,  0, 15,  5, 12, 26, \
  0, 37, 30, 33, 27, 34,  9, 37, 22,  0, \
  0, 24, 30,  0,  0, 38, 23, 25,  0, 30, \
 39, 24, 31,  0,  6, 19, 25,  0, 28, 15, \
  8,  0, 48,  0, 35, 41,  0, 24,  1, 41, \
 31,  0, 35, 21, 15, 26, 15, 27,  4,  0, \
  8,  4,  0,  0,  2, 42, 18,  0, 28, 18, \
 49, 34,  5, 10, 41, 48, 26, 14, 45, 44, \
  9,  0, 49, 50, 24,  0,  0,  0, 23,  0, \
 17,  0, 47, 31,  0, 42,  0,  0,  0, 40, \
 46, 22, 50, 32, 20,  3, 44, 22,  0, 37, \
 25,  0, 19, 26, 14, 23, 27, 41,  0,  1, \
 13,  0, 48, 20, 37,  8,  0, 18,  0, 26, \
 12, 19, 32, 19, 22,  0,  0,  0,  0,  0, \
 16,  0,  0, 43,  0, 10,  5,  0,  6, 26, \
  0, 24, 40, 29,  0, 43, 18, 27,  0,  0, \
 37,  0, 46, 35, 17,  0, 20, 44, 29, 29, \
 40, 33, 22, 27,  0,  0, 38, 21,  4,  0, \
  0, 15, 31, 48, 36, 10,  0, 41,  0, 45, \
 39,  0, 11,  9,  3, 38, 16,  0, 11, 22, \
 37,  0,  3, 44, 10, 12, 47, 22, 32,  7, \
 24,  1,  0, 22, 25,  0, 14,  0,  0,  0, \
 23,  0, 36,  1, 42, 46,  0, 48,  0, 33, \
  5, 27, 45,  0, 15, 29,  0, 50,  2, 31, \
 25,  6, 36, 19, 10, 23,  0, 37,  4,  1, \
  7, 12,  0,  0, 49
""".strip()


def count_non_0_clusters_1(arr):
    """Translate each non-0 to an 'A' char, and 0 to a space.
    Then join together to become a string.
    Then split(), then return number of tokens.
    """
    return len("".join(["A" if e else " " for e in arr]).split())


def count_non_0_clusters_2(arr):
    """groupby() partitions into groups as:
        [[True , [list of non-0]],
         [False, [list of 0s]],
         [True , [list of non-0]],
         [False, [list of 0s]],
              ...
         [True , [list of non-0]]]

        (Old) Next, the list comprenhension iterates thru each tuple,
        then collects the 1st element in each tuple if True.
        Finally, return the len/count of Trues:
            return len([t[0] for t in itertools.groupby(...) if t[0]])

        Next, the list comprenhension iterates thru each tuple,
        then collects the 1st element in each tuple.
        Then return the count() of True elements.
    """
    return [t[0] for t in itertools.groupby(arr, lambda e: bool(e))].count(True)


if __name__ == '__main__':
    a = list(map(int, STDIN_SIO.split(",")))
    # Nicely print it, 10 entries per line, with continuation
    # so can copy-n-paste back into STDIN_SIO
    #print(len(a))
    #for i in range(0, (len(a) // 10) * 10, 10):
    #    print("%3u," * 10 % tuple(a[i:i+10]), end=" \\\n")
    #j = a[(len(a) // 10) * 10:]
    #print("%3u," * (len(j) - 1) % tuple(j[:-1]), end="")
    #print("%3u" % j[-1])
    print("count_*_1() returns", count_non_0_clusters_1(a), "clusters of non-0")
    print("count_*_2() returns", count_non_0_clusters_2(a), "clusters of non-0")
