"""
You are given an undirected graph with n nodes labeled 0 to n-1, and an adjacency list.

Return the number of connected components in the graph.

n = 5
graph = {
  0: [1],
  1: [0, 2],
  2: [1],
  3: [4],
  4: [3]
}

ANSWER : 2
"""

def dfs(node, graph, visited):
    nodes_stack = [node]
    visited.add(node)
    
    while nodes_stack:
        node = nodes_stack.pop()
        neighbors = graph[node]
        for neighbor in neighbors:
            if neighbor not in visited:
                nodes_stack.append(neighbor)
                visited.add(neighbor)

def iterative_dfs(graph):
    visited = set()
    components = 0
    
    for i in range(len(graph)):
        if i not in visited:
            dfs(i, graph, visited)
            components+=1
    
    return components
    

        

    










def dfs_counting(graph, node, visited):
    if not node in visited:
        neighbors = graph[node]
        for neighbor in neighbors:
            visited.add(node)
            dfs_counting(graph, neighbor, visited)


def counting(graph):
    visited = set()
    return dfs_counting(graph,0, visited)

"""
EXECUTION
dfs_counting(graph, 0, {})
0 not in visited
dfs_counting(graph, 1, {0})
1 not in visited
dfs_counting(graph, 0, {0})
return ;
dfs_counting(graph, 2, {0})
2 not in visited
dfs_counting(graph, 1, {0})
return ;
"""