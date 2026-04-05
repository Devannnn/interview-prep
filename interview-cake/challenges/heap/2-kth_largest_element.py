"""
Find the Kth largest element in an unsorted array.
"""

# I maintain a min-heap of size k.
# As I iterate through the array, I push each element.
# If the heap grows beyond k, I remove the smallest element.
# This ensures the heap always contains the k largest elements seen so far.
# At the end, the root of the heap is the kth largest element.

import heapq

def get_kth_largest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]