# Finding prime factor of a number
import math
class Solution:
    def prime_factors(self,n:int)-> list :
        factors=[]

        while n%2==0:
            factors.append(2)
            n//=2
        for i in range(3,int(math.sqrt(n))+1,2):
            while n%i ==0:
                factors.append(i)
                n//=i
        if n>2:
            factors.append(n)
        
        return factors
    
numbers = 315
result = Solution()
print(result.prime_factors(numbers))