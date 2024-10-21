# Prefix Sum algorithm
class Solution : 
    def prefix_sum(self,nums):
        n=len(nums)
        prefix = [0]*n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]
        return prefix
    

def main():
    nums=[1,2,3]
    solution = Solution()
    result = solution.prefix_sum(nums)
    print(result)
if __name__ == "__main__":
    main()


