class Solution:
    def binarySearch(self,nums:list[int],target:int)-> int:
        l,r = 0, len(nums)
        while l<=r:
            m = l + (r-l)//2
            if target <nums[m]:
                r=m-1
            if target > nums[m]:
                l=m+1
            return m
        return -1
    
def main():
    nums=[1,3,4,6,7,9]
    target=7
    solution = Solution()
    result= solution.binarySearch(nums,target)
    print(result)

if __name__=="__main__":
    main()