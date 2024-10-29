class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        dic={}
        duplicates = []
        for _,value in enumerate(nums):
            if value in dic:
                duplicates.append(value)
            else:
                dic[value]=1
        return duplicates
    
solution = Solution()
print(solution.findDuplicates([4,3,2,7,8,2,3,1]))