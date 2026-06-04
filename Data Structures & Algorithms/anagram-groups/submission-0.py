from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        
        for val in strs:
            seen[tuple(sorted(val))].append(val)
        
        return list(seen.values())