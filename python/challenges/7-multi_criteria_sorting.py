"""
Ecris une fonction qui trie une liste de dictionnaire par âge croissant et score décroissant.

Retourne une nouvelle liste.

Par exemple :
users = [
    {"name": "Alice", "age": 30, "score": 90},
    {"name": "Bob", "age": 30, "score": 80},
    {"name": "Charlie", "age": 25, "score": 95},
]

Retourne : 
Charlie (25)
Alice (30, 90)
Bob (30, 80)

"""

def multi_sorting(infos: list[dict]):
    return sorted(infos, key= lambda x: (x["age"], -x["score"]))


users = [
    {"name": "Alice", "age": 30, "score": 90},
    {"name": "Bob", "age": 30, "score": 80},
    {"name": "Charlie", "age": 25, "score": 95},
]

print(multi_sorting(users))