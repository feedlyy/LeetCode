class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False] * len(candies)

        for index, item in enumerate(candies):
            if item + extraCandies >= max(candies):
                result[index] = True

        return result
    
#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75