class Solution:
    def longestPalindrome(self, s: str) -> str:
        #팰린드롬 문자의 수를 짝수/ 홀수로 나눈 후 3칸짜리 포인터와 두칸 짜리 포인터를 이용하여 문제를 풀이함
     
        def expand(left: int, right: int) -> str:  #포인터를 만들기 위한 중첩함수
            while left >= 0 and right <= len(s)-1 and s[left] == s[right]: 
                left -= 1 
                right += 1
            return s[left+1:right]
        
        
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        for i in range(0, len(s)-1):
            result = max(result, 
                            expand(i, i+2),
                            expand(i, i+1),
                            key = len)
        
        return result
            
            
