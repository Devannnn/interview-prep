"""
Merge K sorted lists into one sorted list.
"""

# One way to sort is to put all the elements in a heap and remove them one by one.
# Assuming we use a min-heap, this gives us the elements in ascending order.
# The first loop has a complexity of O(k) 
# The second loop has a complexity of O(n)
# heappush on a heap of size j has a complexity of O(log(j))
# but here we add each element so k*n elements maximum (if all list have the same size)
# So the total time complexity is O(k*n*log(k*n))
# the while loop has a complexity of O(k*n)
# So total complexity is O(k*n + k*n*log(k*n)) = O(k*n*log(k*n))

import heapq

def merge_k_list(k_list):
    k = len(k_list)
    heap = []

    for i in range(k):
        i_list = k_list[i]
        for num in i_list:
            heapq.heappush(heap, num)
    
    ordered_list = []
    while len(heap):
        order_list.append(heapq.heappop(heap))
    
    return order_list

# The first loop has a time complexity of O(k*log(k))
# The second loop go through the heap of length k so O(k)
# Then inside the loop we call heappop and heappush which are both O(log(k))
# So total time complexity is O(2*k*log(k)) = O(k*log(k))
# Space complexity is dominated by the merged_list size which is the total numbers of elements O(n)

def merge_k_list_optimized(k_list):
    heap = []
    k = len(k_list)
    merged_list = []

    for i in range(k):
        curr_list = k_list[i]
        heapq.heappush(heap, (curr_list[0], 0, i))
    
    while heap:
        element, element_index, list_index = heapq.heappop(heap)
        merged_list.append(element)
        curr_list = k_list[list_index]

        if element_index < len(curr_list)-1:
            element_index+=1
            heapq.heappush(heap, (curr_list[element_index], element_index, list_index))
    
    return merged_list