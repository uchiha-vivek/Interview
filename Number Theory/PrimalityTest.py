# checking whether the number is prime or not
#Time complexity is O(N)
import math
class Solution:
    def isPrimeOrNot(self,num:int)->bool:
        
        if num==1:
            return True
        for i in range(2,num):
            if num%i==0:
                return False
        return True
    
    def isPrimeOrNotSquareRootMethod(self,num:int)->bool:
        if num==1:
            return False
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                return False
            return True

    
solution = Solution()
ans = solution.isPrimeOrNot(5)
ans1 = solution.isPrimeOrNotSquareRootMethod(5)
print(ans,ans1)

# Square root Method
# Time Complexity is O(sqr.rootN)

