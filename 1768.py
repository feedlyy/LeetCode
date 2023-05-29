class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        iteration = ""

        if len(word1) > len(word2):
            iteration = word2
        else:
            iteration = word1

        for i in range(len(iteration)):
            result += word1[i] + word2[i]

        if len(word1) == len(word2):
            return result

        if iteration == word1:
            result += word2[len(iteration):]
        else:
            result += word1[len(iteration):]

        return result


#https://leetcode.com/problems/merge-strings-alternately/description/ 