import math
class Solution:
    def sieve_of_eratosthenes(self,num:int) -> list:
        is_prime = [True]*(num+1)
        is_prime[0],is_prime[1]=False,False

        for i in range(2,int(math.sqrt(num)+1)):
                       if is_prime[i]:
                               for j in range(i*i,num+1,i):
                                       is_prime[j]=False # Making it multiples False
        primes = [i for i,prime in enumerate(is_prime) if prime]
        return primes
    
n=30
solution = Solution()
ans = solution.sieve_of_eratosthenes(n)
print(ans)

