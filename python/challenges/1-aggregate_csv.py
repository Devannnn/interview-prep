"""
Problem 2 – Aggregate CSV-like Data

Description:
You receive a list of dictionaries representing file uploads:

Input:
uploads = [
    {"user": "Alice", "type": "pdf", "size": 120},
    {"user": "Bob", "type": "csv", "size": 300},
    {"user": "Alice", "type": "pdf", "size": 80}
]

Write a function that returns the total size of all PDFs per user.

Ouput:
{"Alice": 200, "Bob": 0}
"""
from collections import defaultdict

def get_total_size(uploads):
    sum_dict = defaultdict(int)
    for upload in uploads:
        user, doc_type, size = upload.values()
        if doc_type == "pdf":
            sum_dict[user] += size
    return sum_dict

uploads = [
    {"user": "Alice", "type": "pdf", "size": 120},
    {"user": "Bob", "type": "csv", "size": 300},
    {"user": "Alice", "type": "pdf", "size": 80}
]

print(get_total_size(uploads))