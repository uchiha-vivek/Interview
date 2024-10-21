class Solution :
    def find_all_subarrays(self,arr):
        n=len(arr)
        subarrays = []
        for i in range(n):
            for j in range(i,n):
                subarray = arr[i:j+1]
                subarrays.append(subarray)
        return subarrays

def main():
    arr = [1,2,3]
    solution = Solution()
    result =solution.find_all_subarrays(arr)
    print(result)

if __name__=="__main__":
    main()
