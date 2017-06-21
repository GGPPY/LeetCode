#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/27 17:23
# @Author  : ppy
# @Site    : 
# @File    : Longest Substring Without Repeating Characters.py
# @Software: PyCharm
"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Subscribe to see which companies asked this question.

Show Tags
Show Similar Problems
"""


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        max_length = 0
        m = {}
        for i in xrange(len(s)):
            if s[i] in m and start <= m[s[i]]:
                start = m[s[i]] + 1
            else:
                if i - start + 1 > max_length:
                    max_length = i - start + 1
            m[s[i]] = i
        return max_length


if __name__ == "__main__":
    print Solution().lengthOfLongestSubstring('abcabcbb')