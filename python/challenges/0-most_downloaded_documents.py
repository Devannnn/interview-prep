"""
Problem 1 – Most Downloaded Documents

Description:
You receive a list of download events as tuples: (user_id, document_id). 
Return the top N most downloaded documents, sorted by count descending.

Input :
downloads = [
    ("user1", "doc1"),
    ("user2", "doc2"),
    ("user1", "doc1"),
    ("user3", "doc1"),
    ("user2", "doc2")
]
N = 2
"""
from collections import defaultdict

def get_most_downloaded(downloads, n):
    frequency_map = defaultdict(int)
    for (user, doc) in downloads:
        frequency_map[doc]+=1
    ordered_list = sorted(frequency_map.items(), key=lambda x : x[1], reverse=True)
    if n > len(ordered_list):
        raise ValueError(f'${n} is higher than the number of documents')
    return ordered_list[0:n]


inputs = [
    ("user1", "doc1"),
    ("user2", "doc2"),
    ("user1", "doc1"),
    ("user3", "doc1"),
    ("user2", "doc2")
]

print(get_most_downloaded(inputs, 2))