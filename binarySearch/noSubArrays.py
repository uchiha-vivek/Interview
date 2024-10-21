class Solution:
    def SubArrays(self,nums:list)-> list:
        n = len(nums)
        subarrays=[]
        for i in range(n):
            for j in range(i,n):
                subarray = nums[i:j+1]
                subarrays.append(subarray)
        return subarrays

    def NumberOfSubArrays(self,nums:list)-> int:
        ans = len(nums)
        return ans

def main():
    nums=[1,2,3]
    solution =Solution()
    subarray = solution.SubArrays(nums)
    result = solution.NumberOfSubArrays(subarray)
    print(result)

if __name__=="__main__":
    main()