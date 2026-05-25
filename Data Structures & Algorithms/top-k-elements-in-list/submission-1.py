class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        sorted_items = sorted(
            frequency.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return [num for num, _ in sorted_items[:k]]


        


