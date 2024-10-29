import time
class Solution :
    def missingNumber(self,nums:list[int])-> int:
        nums.sort()
        for index,value in enumerate(nums):
            if index !=value:
                return value-1
            if value == len(nums)-1:
                return value+1
    def missingNumber1(self,nums:list[int]) -> int:
        return sum(range(len(nums+1))) - sum(nums)
        pass

solution = Solution()
start = time.time()
print(solution.missingNumber([3,0,1]))
end=time.time()
elapse  = end-start
print(elapse) 