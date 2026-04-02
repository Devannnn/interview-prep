"""
Écris une fonction qui :

Garde uniquement les documents "approved"

Les trie par title alphabétique

Retourne une liste de strings formatées comme :
"1 - Spec A"
"3 - Spec C"

Exemple :
documents = [
    {"id": 1, "title": "Spec A", "status": "approved"},
    {"id": 2, "title": "Spec B", "status": "pending"},
    {"id": 3, "title": "Spec C", "status": "approved"},
    {"id": 4, "title": "Spec D", "status": "rejected"},
]

"""

def format_documents(documents: list[dict]):
    approved_documents = filter(lambda x: x["status"] == "approved", documents)
    sorted_documents = sorted(approved_documents, key= lambda x: x["title"])
    return [str(doc["id"]) + " - " + doc["title"] for doc in sorted_documents]


documents = [
    {"id": 1, "title": "Spec A", "status": "approved"},
    {"id": 2, "title": "Spec B", "status": "pending"},
    {"id": 3, "title": "Spec C", "status": "approved"},
    {"id": 4, "title": "Spec D", "status": "rejected"},
]

print(format_documents(documents))