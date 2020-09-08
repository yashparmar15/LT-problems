class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low = 0
        high = int(sqrt(c))
        while low <= high:
            sum = low**2 + high**2
            if sum < c:
                low += 1
            if sum > c:
                high -= 1
            if sum == c:
                return True
        return False
                
