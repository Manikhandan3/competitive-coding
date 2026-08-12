class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums)+1)]
        count = Counter(nums)
        for key,v in count.items():
            freq[v].append(key)
        res = []
        for i in range(len(freq)-1,0,-1):
            for f in freq[i]:
                res.append(f)
                if len(res) == k:
                    return res
