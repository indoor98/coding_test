#브루트 포스 풀이
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                  
#in을 이용한 탑색
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n
            
            if complement in nums[i+1:]:
                return nums.index(n), nums[i+1:].index(complement) + (i + 1)
              
# 딕셔너리 이용
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {} #딕셔너리 변수 선언
        for i, num in enumerate(nums): #key와 value를 반대로 바꿔서 딕셔너리에 저장
            nums_map[num] = i
            
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return nums.index(num), nums_map[target - num]
            
