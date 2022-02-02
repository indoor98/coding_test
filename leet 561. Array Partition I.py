#내 풀이
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()
        i = 0
        while i <= len(nums)-1:
            sum += nums[i]
            i += 2
        
        return sum
            
