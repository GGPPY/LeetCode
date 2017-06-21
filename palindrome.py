#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/22 16:02
# @Author  : ppy
# @Site    : 
# @File    : palindrome.py
# @Software: PyCharm
"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be
built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
    "abccccdd"

Output:
7

Explanation:

One longest palindrome that can be built is "dccaccd", whose length is 7.

"""


s = """civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefieml
doftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmigh
tliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthis
groundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllitt
lenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnf
inishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbef
oreusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatwehereh
ighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthe
peoplebythepeopleforthepeopleshallnotperishfromtheearth"""


class Solution(object):

    def longestPalindrome(self, s):
        m = {}
        for c in s.replace('\n', ''):
            if c not in m:
                m[c] = 0
            m[c] += 1
            # m[c] = 1 if c not in m else m[c]+1
        single = 0
        result = 0
        for i in m.itervalues():
            result += i
            if i % 2 == 1:
                single += 1
        if single:
            return result - single + 1
        else:
            return result

if __name__ == '__main__':
    assert Solution().longestPalindrome('abccccdd') == 7
