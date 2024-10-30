class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        temp = sorted(nums)
        d={}
        for i,num in enumerate(temp):
            if num not in d:
                d[num] = i
        result = []
        for i in nums:
            result.append(d[i])
        return result
    
solution= Solution()
print(solution.smallerNumbersThanCurrent([8,1,2,2,3]))
        
        