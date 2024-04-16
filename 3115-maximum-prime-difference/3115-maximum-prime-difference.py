class Solution:
    
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def is_prime(x):
            if x == 1 :
                return False
            for i in range(2, x):
    	        if x % i == 0:
        	        return False
            return True
        
        prime_nums = []
        for i, n in enumerate(nums):
            if is_prime(n):
                prime_nums.append(i)
        if len(prime_nums) == 1:
            return 0
        
        else:    
            return prime_nums[-1] - prime_nums[0]