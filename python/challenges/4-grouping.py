"""
Ecris une fonction pour grouper le montant par utilisateur.

Par exemple :

orders = [
    {"user": "Alice", "amount": 50},
    {"user": "Bob", "amount": 30},
    {"user": "Alice", "amount": 20},
    {"user": "Bob", "amount": 70},
]

devient 
{
    "Alice": 70,
    "Bob": 100
}


"""

def grouping(orders: list[dict]):
    groups = {}
    for order in orders:
        user = order["user"]
        amount = order["amount"]
        if user not in groups:
            groups[user] = amount
        else:
            groups[user] += amount
        
    return groups



orders = [
    {"user": "Alice", "amount": 50},
    {"user": "Bob", "amount": 30},
    {"user": "Alice", "amount": 20},
    {"user": "Bob", "amount": 70},
]

print(grouping(orders))