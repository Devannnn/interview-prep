"""
Tu dois écrire une fonction qui valide les payloads fournit par l'utilisateur.

Écris une fonction qui :
- Ignore les payloads sans "value"
- Lève une exception si "value" < 0
- Retourne la somme des valeurs valides

Par exemple :
payloads = [
    {"id": 1, "value": 10},
    {"id": 2},
    {"id": 3, "value": -5},
]
"""



def validate_payloads(payloads: list[dict]):
    sum_values = 0

    for payload in payloads:
        try:
            value = payload["value"]
            if value < 0:
                raise ValueError("Negative values are not allowed")
            sum_values += value
        except KeyError:
            continue
    
    return sum_values

payloads = [
    {"id": 1, "value": 10},
    {"id": 2},
    {"id": 3, "value": -5},
]

print(validate_payloads(payloads))