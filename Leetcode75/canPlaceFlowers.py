


def canPlaceFlowers(flowerbed,n):
        """
        :type flowerbed: List[int] 1/0 
        :type n: int
        :rtype: bool
        """
        count = 0
        i=1
        if n ==0:
            return True
        if n>len(flowerbed)/2+1:
             return False

        if(len(flowerbed)==1):
            if n==1 and flowerbed[0] ==0:
                 return True
            else:
                 return False

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            count +=1
            flowerbed[0] =1

        while i < len(flowerbed)-1:
            if flowerbed[i] == flowerbed[i-1] and flowerbed[i] == flowerbed[i+1] and flowerbed[i] == 0:
                 flowerbed[i] = 1
                 count+=1
            i+=1

            if count == n: 
                return True

        if flowerbed[len(flowerbed)-1] == 0 and flowerbed[len(flowerbed)-2] == 0:      
            flowerbed[len(flowerbed)-1] = 1  
            count+=1
            if count == n: 
                return True  
        if count == n: 
                return True  

        return False

flowerbed = [0,0]
n = 1
print(canPlaceFlowers(flowerbed, n))