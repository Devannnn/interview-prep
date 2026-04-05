"""
Given an undirected graph with maximum degree D, 
find a graph coloring using at most D+1 colors.
"""

class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None


a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')

a.neighbors.add(b)
b.neighbors.add(a)
b.neighbors.add(c)
c.neighbors.add(b)

graph = [a, b, c]

def generate_d_colors(d):
    # Fake function. We could generate variation of the same hex color
    # But I guess using a library would work best here to generate real colors
    return [1]*d

def get_possible_color(neighbors, palette):
    for color in palette:
        can_be_used = True
        for neighbor in neighbors:
            if neighbor.color == color:
                can_be_used = False
        if can_be_used:
            return color
    raise ValueError("No color assigned")


def bfs(node, graph, palette):
    if node.color is not None:
        neighbors = node.neighbors
        node.color = get_possible_color(neighbors, palette)
        for neighbor in neighbors:
            bfs(neighbor, graph, palette)


def graph_coloring(graph, d):
    palette = generate_d_colors(d+1)
    bfs(node, graph, palette)
    return graph




def optimized_graph_coloring(graph, colors):

    for node in graph:

        if node in node.neighbors:
            raise ValueError('Loop')
        
        illegal_colors = set([neighbor.color for neighbor in node.neighbors if neighbor.color])

        for color in colors:
            if color not in illegal_colors:
                node.color = color
                break



