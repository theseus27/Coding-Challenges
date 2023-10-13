# EASY
# Runtime: 36 ms (Beat 62.68%)
# Memory: 13.9 MB (Beat 79.4%)

""" QUESTION
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

from typing import List

def longestCommonPrefix(self, strs: List[str]) -> str:
    result = ""

    if len(strs) == 0: 
        return result

    for i in range(len(strs[0])):
        for j in range(len(strs)):
            if len(strs[j]) <= i or strs[j][i] != strs[0][i]:
                return result
        result += strs[0][i]

    return result