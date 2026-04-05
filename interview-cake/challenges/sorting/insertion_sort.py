### ENONCE
# Implements the insertion sorting algorithm.

### CODE

def insertion_sort(list):
    for i in range(1, len(list)):
        compteur = i
        while (compteur > 0) and list[compteur] < list[compteur-1]:
            tmp = list[compteur]
            list[compteur] = list[compteur-1]
            list[compteur-1] = tmp
            compteur-=1


### TESTS
input = [5, 2, 7, 1, 8, 3, 9, 4, 6]
output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
insertion_sort(input)
print(input == output, input)

input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
insertion_sort(input)
print(input == output, input)

input = [9, 8, 7, 6, 5, 4, 3, 2, 1]
output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
insertion_sort(input)
print(input == output, input)

input = [3, 2, 4, 3, 1, 2, 4, 3, 1]
output = [1, 1, 2, 2, 3, 3, 3, 4, 4]
insertion_sort(input)
print(input == output, input)

input = [-5, 2, -7, 1, 0, 3, -9, 4, -6]
output = [-9, -7, -6, -5, 0, 1, 2, 3, 4]
insertion_sort(input)
print(input == output, input)

input = []
output = []
insertion_sort(input)
print(input == output, input)

input = [5]
output = [5]
insertion_sort(input)
print(input == output, input)