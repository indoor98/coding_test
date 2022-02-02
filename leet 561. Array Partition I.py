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
            
#enumerate 사용 (위 코드보다 조금 더 빠름)
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()
        i = 0
        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n
        return sum

#파이썬다운 방식(슬라이싱 활용)
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

    #슬라이싱은 굉장히 빠르고 간결하다.
