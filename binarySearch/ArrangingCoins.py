# class Solution:
#     def ArrangeCoins(self,n:int) -> int :
#         rows=0
#         coins_used=0
#         while coins_used + (rows+1)<=n:
#             rows+=1
#             coins_used+=rows
#         return rows

        


# def main():
#     n=5
#     solution=Solution()
#     result=solution.ArrangeCoins(n)
#     print(result)


# if __name__=="__main__":
#     main()


class Solution:
    def ArrangeCoins(self,n:int) -> int :
        l,r = 1,n
        res=0
        while l<=r:
            mid = (l+r)//2
            coins= (mid/2) * (mid+1)
            if coins > n :
                r= mid-1
            else :
                l=mid+1
                res=max(mid,res)
        return res


def main():
    n=5
    solution=Solution()
    result =solution.ArrangeCoins(n)
    print(result)

if __name__=="__main__":
    main()