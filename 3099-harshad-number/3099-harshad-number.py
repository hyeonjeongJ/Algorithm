class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        def d(x):
            sum = 0
                
            while x > 0 :
	            sum += x % 10
	            x = x // 10
            return sum
        
        r_sum = d(x)
        if x % r_sum == 0:
            return r_sum
        else:
            return -1