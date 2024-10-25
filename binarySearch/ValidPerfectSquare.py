class Solution:
    def ValidPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False
        if num == 0 or num == 1:
            return True
        
        l, r = 1, num  # Set the left and right bounds for binary search
        while l <= r:
            mid = (l + r) // 2
            mid_squared = mid * mid
            
            if mid_squared == num:
                return True
            elif mid_squared < num:
                l = mid + 1
            else:
                r = mid - 1
        
        return False  # Return False if no perfect square is found

def main():
    num = 9
    solution = Solution()
    result = solution.ValidPerfectSquare(num)
    print(result)

if __name__ == "__main__":
    main()
