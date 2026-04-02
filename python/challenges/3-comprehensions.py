"""
Transforme cette liste :

data = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 42},
    {"name": "Charlie", "score": 73}
]

en un dictionnaire {name: score} uniquement pour les scores >= 50 en utilisant une comprehension.
"""

def transform_dict_normal(scores: list[dict]):
    new_scores = {}
    for element in scores:
        if element["score"] >= 50:
            new_scores[element["name"]] = element["score"]
    return new_scores

def transform_dict_comprehension(scores: list[dict]):
    return {
        element["name"] : element["score"]
        for element in scores
        if element["score"] >= 50
    }


data = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 42},
    {"name": "Charlie", "score": 73}
]


print(transform_dict_normal(data))
print(transform_dict_comprehension(data))