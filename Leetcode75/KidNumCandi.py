def kidsWithCandies( candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]

        """
        
        max_kid = max(candies)
        out = [(max_kid-extraCandies)<=i  for i in candies]
        return out

candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies,extraCandies)) 
