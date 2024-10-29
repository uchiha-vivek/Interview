import time

class Solution:
    def ContainsDuplicate(self,nums:list[int])-> bool :
        if len(set(nums)) == len(nums):
            return True
        else :
            return False



solution = Solution()
start  = time.time()
print(solution.ContainsDuplicate([1,2,3]))
end = time.time()
elapse = end-start
print(elapse)