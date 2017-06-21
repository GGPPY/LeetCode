#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/21 15:00
# @Author  : ppy
# @Site    : 
# @File    : Range Addition II.py
# @Software: PyCharm
"""
Given an m * n matrix M initialized with all 0's and several update operations.

给你一个所有元素都为0, M * N 的矩阵， 以及一些更新操作。

Operations are represented by a 2D array, and each operation is represented by an array with two positive integers

操作用2d矩阵表示，每一个操作都用一个包含两个正整数的数组表示： [a ,b].

a and b, which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.

意味着所有满足 0 <= i <a ,0<= j < b 的 m[i][j]都要+1 s.

You need to count and return the number of maximum integers in the matrix after performing all the operations.

经过这些操作，你需要求出矩阵中最大整数的个数。

Example 1:
Input:
m = 3, n = 3
operations = [[2,2],[3,3]]
Output: 4
Explanation:
Initially, M =
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]

After performing [2,2], M =
[[1, 1, 0],
 [1, 1, 0],
 [0, 0, 0]]

After performing [3,3], M =
[[2, 2, 1],
 [2, 2, 1],
 [1, 1, 1]]

So the maximum integer in M is 2, and there are four of it in M. So return 4.

Note:

The range of m and n is [1,40000].
The range of a is [1,m], and the range of b is [1,n].
The range of operations size won't exceed 10,000.

采用面积法解决。

"""


class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        width = min(min([x[0] for x in ops]), m)
        high = min(min([x[1] for x in ops]), n)
        return width * high


if __name__ == '__main__':
    print Solution().maxCount(3, 3, [])
