# Iterative Implementation
class Solution:
    def power(self, a: int, b: int) -> int:
        result = 1
        while b:
            if b & 1:  # If b is odd
                result *= a  # Multiply result with a
            a *= a  # Square the base
            b >>= 1  # Divide b by 2
        return result

solution = Solution()
print(solution.power(2, 8))  # Output: 256
