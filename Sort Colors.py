#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/24 15:12
# @Author  : ppy
# @Site    : 
# @File    : Sort Colors.py
# @Software: PyCharm
"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's
and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?

"""


class Solution(object):

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums) - 1
        p = 0
        while p <= end:
            if nums[p] == 2:
                nums[end], nums[p] = nums[p], nums[end]
                end -= 1
            elif nums[p] == 0:
                nums[start], nums[p] = nums[p], nums[start]
                start += 1
                p += 1
            else:
                p += 1
            print nums

if __name__ == '__main__':
    Solution().sortColors([0, 1, 2, 0, 2, 0, 1, 2, 0, 1, 2])


