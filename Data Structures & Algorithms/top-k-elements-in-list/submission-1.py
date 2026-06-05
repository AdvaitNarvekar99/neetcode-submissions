from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums).most_common()
        result = []
        for i in range(0,k):
            result.append(cnt[i][0])
        return result