class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        value = []
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
        ans = list(dict(sorted(seen.items(), key=lambda item: item[1], reverse=True)).keys())

        print(ans)
        return ans[:k]
    