Graph Coloring using Backtracking

Write a Python program to color the vertices of a given graph using the Backtracking algorithm. The program should assign colors to each vertex such that no two adjacent vertices have the same color. Finally, display the color assigned to each vertex and the minimum number of colors used.

Given Graph
Vertices: A, B, C, D, E
Edges: A-B, A-C, A-D, B-C, B-D, C-D, D-E
Available colors: R, G, B, O, Y, I, V

 graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'B', 'C', 'E'],
    'E': ['D']
}

colors = ['R', 'G', 'B', 'O', 'Y', 'I', 'V']

result = {}

def is_safe(vertex, color):
    for neighbor in graph[vertex]:
        if result.get(neighbor) == color:
            return False
    return True

def color_graph(index):
    vertices = list(graph.keys())

    if index == len(vertices):
        return True

    vertex = vertices[index]

    for color in colors:
        if is_safe(vertex, color):
            result[vertex] = color

            if color_graph(index + 1):
                return True

            del result[vertex]

    return False

color_graph(0)

print("Color Assignment:")

for vertex, color in result.items():
    print(vertex, "->", color)

print("Minimum Colors Used:", len(set(result.values())))

output 
Color Assignment:
A -> R
B -> G
C -> B
D -> O
E -> R
Minimum Colors Used: 4
