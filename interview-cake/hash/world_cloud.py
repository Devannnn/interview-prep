### ENONCE
# Write code that takes a long string and builds its word cloud data in a dictionary, 
# where the keys are words and the values are the number of times the words occurred.

### CODE
def word_cleaner(word):
    if (word[-1] == "'") or (word[-1] == ".") or (word[-1] == ","):
        word = word[:len(word)-1]
    if (word[len(word)-2:] == "'s"):
        word = word[:len(word)-2]
    return word.casefold()

def world_cloud(input):
    dict = {}
    words = input.split(" ")
    for word in words:
        cleaned_word = word_cleaner(word)
        if (dict.get(cleaned_word) == None):
            dict.update({cleaned_word : 1})
        else:
            compteur = dict.get(cleaned_word)
            dict.update({cleaned_word : compteur+1})
    return dict

### TESTS
input = 'After beating the eggs, Dana read the next step:'
print(world_cloud(input))

input = 'Add milk and eggs, then add flour and sugar.'
print(world_cloud(input))

input = 'Add milk and eggs, then add flour and sugar.'
print(world_cloud(input))

input = 'You are a short-termed person.'
print(world_cloud(input))

input = "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake. The bill came to five dollars."
print(world_cloud(input))