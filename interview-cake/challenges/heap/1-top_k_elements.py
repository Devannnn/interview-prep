"""
Return the top K largest/smallest elements from an array.
"""

# Answer : I could sort the array and then takes the K first element.
# The best sorting algorithm have a complexity of O(n*log(n)) where n is the array's length
# Or I could use a heap.
# A heap allows to get the min/max in O(1)
# So if we maintain a heap of the kth largest/smallest element, we can discard invalid candidate in log(k)
# Because we are going to add every element of the list, the total complexity will be O(n*log(k))
# If k<<n, which will often be the case, heap is much more efficient.
import heapq


def get_k_smallest_elements(elements, k):
    heap = []

    for element in elements:
        heapq.heappush(heap, -element)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [-x for x in heap]


# min heap
def get_k_largest_elements(elements, k):
    heap = []

    for element in elements:
        heapq.heappush(heap, element)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap