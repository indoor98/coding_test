class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        # i 를 기준으로 왼쪽에 있는 수들을 곱한다
        for i in range(0, len(nums)):
            out.append(p)
            p = p*nums[i]
        
        p = 1
        # 오른쪽에 있는 수들을 차례로 곱한다.
        for i in range(len(nums)-1, -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        
        return out
