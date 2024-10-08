# Time complexity - O(nlogk) with min heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap,num)
            if len(heap) > k:
                heappop(heap)
        return heappop(heap)
