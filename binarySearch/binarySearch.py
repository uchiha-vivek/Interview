class Solution :
    def binarySearch(self,nums:list[int],target:int) -> int :
        l,r= 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]<target:
                l=mid+1
            elif nums[mid]>target:
                r=mid-1
            else :
                return mid
        return -1
def main():
    nums=[1,2,4,6,7]
    target=7
    solution =Solution()
    result = solution.binarySearch(nums,target)
    print(result)

if __name__=="__main__":
    main()