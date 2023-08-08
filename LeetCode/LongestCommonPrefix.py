class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        matchingChar = ""
        charPos = 0
        if(strs.__len__() == 1):
            return strs[0]
        for j in range(10000):
            matchingChar = ""
            for i in range(0,strs.__len__()-1):
                word_1 = strs[i]
                word_2 = strs[i+1]
                try:
                    if(word_1[charPos] == word_2[charPos]):
                        matchingChar = word_1[charPos];
                    else: 
                        return prefix
                except:
                    return prefix
            charPos+=1
            prefix+=matchingChar
        return prefix


# https://leetcode.com/problems/longest-common-prefix/