class Solution :
    def SumArray(self,nums:list)-> int :
        n =len(nums)
        sum_array = []
        sub_array = []
        for i in range(n):
            for j in range(i,n):
                 
                sumArray= sum(nums[i:j+1])
                sum_array.append(sumArray)
        return sum_array



def main():
    nums=[1,2,3]
    solution=Solution()
    result = solution.SumArray(nums)
    print(result)

if __name__ == "__main__":
    main()