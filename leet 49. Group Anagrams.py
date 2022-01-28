class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            anagrams[''.join(sorted(word))].append(word) #sorted를 할 경우 리턴값이 어떤 모양일까?
        
        return anagrams.values()
