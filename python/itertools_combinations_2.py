# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 00:39:20 2019

@author: Ham

HackerRanch Challenge: Iterable and Iterators

The itertools module standardizes a core set of fast, memory efficient tools
that are useful by themselves or in combination.
Together, they form an iterator algebra making it possible to construct
specialized tools succinctly and efficiently in pure Python.

To read more about the functions in this module, check out their documentation here.

You are given a list of N lowercase English letters.
For a given integer k, you can select any k indices (assume 1-based indexing)
with a uniform probability from the list.

Find the probability that at least one of the K indices selected will contain the letter: 'a'.

Input Format

The input consists of three lines.
The first line contains the integer N, denoting the length of the list.
The next line consists of N space-separated lowercase English letters,
denoting the elements of the list.

The third and the last line of input contains the integer k,
denoting the number of indices to be selected.

Output Format

Output a single line consisting of the probability
that at least one of the  indices selected contains the letter:'a'.

Note: The answer must be correct up to 3 decimal places.

Constraints



All the letters in the list are lowercase English letters.

Sample Input

4
a a c d
2

Sample Output

0.8333

Explanation

All possible unordered tuples of length 2 comprising of indices from 1 to 4 are:

(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), and (3, 4)

Out of these 6 combinations, 5 of them contain either
index 1 or index 2 which are the indices that contain the letter 'a'.

Hence, the answer is 5/6.

"""

import itertools

if __name__ == '__main__':
    n = int(input().strip())
    #w = [p for p, l in enumerate(input().strip().split(), 1) if l == 'a']
    #print(w)
    #k = int(input().strip())
    #a = 0
    #for c, t in enumerate(itertools.combinations(range(1, n + 1), k), 1):
    #    for i in t:
    #        if i in w:
    #            a += 1
    #            #print(c, t, a)
    #            break
    #
    # Above is my original, and working submission
    # Below is a revision after reading the Discussion forum
    # I optimized to iterate thru the combo(w, k) only once.
    # Other solution might iterate thru 3 times: 1st to make it a list;
    # 2nd to iterate thru the list; then 3rd to calculate len of the list.
    # The c, t in enumerate(iterable, 1) is such that at the end,
    # c will be the length of the iterable.
    # Caution: if someone tries to convert the "for" loop to a list comp,
    # then (for Python 3), both "c" and "t" are NOT be defined
    # after the list comprehension!
    #
    w = input().strip().split()
    k = int(input().strip())
    #print(k, w)
    a = 0
    for c, t in enumerate(itertools.combinations(w, k), 1):
        #print(c, t)
        if 'a' in t:
            a += 1
    #print(a, c)
    print("%.12f" % (float(a) / float(c)))
