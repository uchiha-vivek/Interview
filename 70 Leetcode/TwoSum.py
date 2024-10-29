class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        n=len(nums)
        for i in range(n):
            compliment = target-nums[i]
            if compliment in hash_map:
                return [hash_map[compliment],i]
            hash_map[nums[i]]=i
        return []
        
solution = Solution()
print(solution.twoSum([2,11,7,15],9))