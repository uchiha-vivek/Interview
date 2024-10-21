class Solution:
    def splitArray(self, nums: list[int], m: int) -> int:
        l, r = max(nums), sum(nums)
        res = r
        
        def canSplit(largest):
            subArray = 1
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subArray += 1
                    curSum = n
                    if subArray > m:
                        return False
            return True
        
        while l <= r:
            mid = l + (r - l) // 2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
                
        return res

def main():
    nums=[7,2,5,10,8]
    m=2
    solution = Solution()
    result = solution.splitArray(nums,m)
    print(result)

if __name__=='__main__':
    main()