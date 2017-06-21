#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/23 9:20
# @Author  : ppy
# @Site    : 
# @File    : Longest Palindromic Substring.py
# @Software: PyCharm
"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"

Input : "bbbb"

"""


class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return None
        length = 1
        start = 0
        for i in xrange(len(s)):
            if i - length >= 1 and s[i - length-1:i+1] == s[i-length-1:i+1][::-1]:
                start = i - length - 1
                length += 2
                continue

            if i - length >= 0 and s[i-length:i+1] == s[i-length:i+1][::-1]:
                start = i - length
                length += 1
        return s[start:start+length]


if __name__ == '__main__':
    print Solution().longestPalindrome('babad')
