class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for key in nums:
            if key not in freq:
                freq[key] =0
            freq[key] = freq[key] + 1
        
        sorted_freq = sorted(freq.items() , key=lambda item:item[1], reverse = True)

        ans = []

        for value in range(k):
            ans.append(sorted_freq[value][0])
        return ans