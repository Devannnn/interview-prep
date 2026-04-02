### ENONCE
# Implements the quick sorting algorithm.

### CODE

def exchange(list, i, j):
    tmp = list[i]
    list[i] = list[j]
    list[j] = tmp

def partition(list, begin, end, pivot):
    exchange(list, pivot, len(list)-1)
    indice_partition = begin
    compteur = 0

    while list[indice_partition] > list[-1]:


def select_pivot(list):
    return len(list)//2

def quick_sort(list, begin, end):
    if begin < end:
        pivot = select_pivot(list[begin:end])
        indice = partition(list, begin, end, pivot)
        quick_sort(list, begin, indice)
        quick_sort(list, indice+1, end)

def sorting(list):
    quick_sort(list, 0, len(list))

### TESTS
input = [5, 2, 7, 1, 8, 3, 9, 4, 6]
output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sorting(input)
print(input == output, input)

input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sorting(input)
print(input == output, input)

input = [9, 8, 7, 6, 5, 4, 3, 2, 1]
output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sorting(input)
print(input == output, input)

input = [3, 2, 4, 3, 1, 2, 4, 3, 1]
output = [1, 1, 2, 2, 3, 3, 3, 4, 4]
sorting(input)
print(input == output, input)

input = [-5, 2, -7, 1, 0, 3, -9, 4, -6]
output = [-9, -7, -6, -5, 0, 1, 2, 3, 4]
sorting(input)
print(input == output, input)

input = []
output = []
sorting(input)
print(input == output, input)

input = [5]
output = [5]
sorting(input)
print(input == output, input)