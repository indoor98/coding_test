#해쉬 테이블을 이용한 풀이
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = {} # 해쉬테이블로 딕셔너리를 선언
        count = 0
        for char in stones :
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1
                
        for char in jewels:
            count += freqs[char]
            
        return count

#defaultdict를 이용한 비교 생략
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0
        
        #defaultdict로 선언하면 굳이 not in stones 를 따질 필요가 없어 진다.
        for char in stones:
            freqs[char] += 1
        
        for char in jewels:
            count += freqs[char]
            
        return count
      
#Counter 모듈 이용
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(S)
        count = 0
        for char in jewels:
            count += freqs[char]
            
        return count
      
      
#파이썬다운 방식

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)
    
