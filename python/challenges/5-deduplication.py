"""

emails = [
    "alice@example.com",
    "bob@example.com",
    "alice@example.com",
    "charlie@example.com",
]

Objectif : Retourner la liste des emails uniques en conservant l’ordre d’apparition.
"""

def deduplication_naive(emails: list[str]):
    # Isn't enough because set are unordered => elements can be placed differently each time you access the set
    return set(emails)

def deduplication(emails: list[str]):
    elements = {}
    for email in emails:
        if email not in elements:
            elements[email] = 1
    return list(elements.keys())

emails = [
    "alice@example.com",
    "bob@example.com",
    "alice@example.com",
    "charlie@example.com",
]

print(deduplication(emails))