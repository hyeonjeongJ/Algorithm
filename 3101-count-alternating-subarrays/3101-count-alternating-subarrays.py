class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        count = 1 #nums[0]
        start = 0
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                start = i
            count += i - start + 1
        return count
        