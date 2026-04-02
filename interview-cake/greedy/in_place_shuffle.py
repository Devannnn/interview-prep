### ENONCE
# Write a function for doing an in-place ↴ shuffle of a list.
# The shuffle must be "uniform," meaning each item in the original 
# list must have the same probability of ending up in each spot in the final list.
# Assume that you have a function get_random(floor, ceiling) for getting a random 
# integer that is >= floor and <= ceiling.

### CODE
import random

def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

def exchange(list, old, new):
    tmp = list[old]
    list[old] = list[new]
    list[new] = tmp

def generate_new_indices(len_list):
    new_indices = []
    remaining_indices = [i for i in range(len_list)]
    taille = len(remaining_indices)-1
    while taille >= 0:
        new_indice = get_random(0, taille)
        new_indices.append(remaining_indices[new_indice])
        remaining_indices.pop(new_indice)
        taille = taille - 1
    return new_indices

def shuffle(the_list):
    len_list = len(the_list)
    new_indices = generate_new_indices(len_list)
    for i in range(len_list):
        exchange(the_list,i,new_indices[i])


### TESTS
sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)

### COMPLEXITY
# O(n) time
# O(n) space