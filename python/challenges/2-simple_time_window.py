"""
Problem 3 – Simple Time Window Analysis

Description:
You receive a list of timestamped events for a document repository:

Input:
events = [
    "2026-03-08T12:10:01",
    "2026-03-08T12:10:05",
    "2026-03-08T12:11:10"
]

Return a dictionary with count of events per minute:
Output:
{
    "2026-03-08T12:10": 2,
    "2026-03-08T12:11": 1
}

"""
from collections import defaultdict

def count_events(events: list[str]) -> dict[str, int]:
    counter = defaultdict(int)

    for event in events:
        minute = event[:-2]
        counter[minute] += 1
    
    return counter

events = [
    "2026-03-08T12:10:01",
    "2026-03-08T12:10:05",
    "2026-03-08T12:11:10"
]

print(count_events(events))