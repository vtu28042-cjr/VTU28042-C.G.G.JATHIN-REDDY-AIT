1.Problem Statement:

Given an undirected graph represented as an adjacency list and a starting node, write a program to perform a Breadth-First Search (BFS) traversal starting from that node and print all visited nodes in the order they are traversed.

Example:

Graph Structure: Node A is connected to B and C.

Input: A

Output: BFS Traversal: A B C

from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A']
}

def bfs(start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

start = input("Enter starting node: ")

print("BFS Traversal:")
bfs(start)
2.
Problem Statement:

Write a program to traverse a connected graph starting from a chosen node using Depth First Search (DFS). Print every reachable node once in the order it is visited.

Task:

Take a starting node as input from the user (for example, 'A').

Visit the starting node and move to its first neighbor.

Keep going deeper into unvisited neighbors before coming back.

Print each node as you visit it without repeating any node.

Example:

Starting Node: A

Output: A B C
graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A']
}

visited = set()

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in graph[node]:
            dfs(neighbour)

start = input("Enter starting node: ")

print("DFS Traversal:")
dfs(start)


SCENARIO 1

Problem Statement
Title: Simulate CDN Cache Invalidation Using Breadth-First Search (BFS)

Description:

Simulate how a cache invalidation command spreads through a network of Content Delivery Network (CDN) servers starting from a central master server. Each network hop takes 1 second to propagate. If a server is offline, the invalidation signal stops at that node, leaving its downstream servers unreached.

Task
Start at the master server at 0 seconds.

Spread the signal level-by-level (BFS) to connected servers.

Skip any server that is listed in offline_nodes and log it as a point of failure.

Calculate:

Total Propagation Time: The maximum time taken to reach the farthest online server.

Node Invalidation Times: The exact second each server receives the signal.

Failed Subtree Roots: Offline servers that blocked further propagation.

Example (Using Provided Data)
CDN Network: master → Reg1, Reg2, Reg3

Offline Servers: {"Reg2"}



from collections import deque


def invalidate_cdn_cache(graph, master_node, offline_nodes):
    """
    Performs level-order BFS to simulate CDN cache invalidation.

    Returns:
        total_time      -> Time required for propagation
        visited_times   -> Invalidation time of each node
        failed_subtrees -> Nodes that could not be reached
    """

    visited = {master_node: 0}
    queue = deque([master_node])
    failed_subtrees = set()

    
    if master_node in offline_nodes:
        return 0, {}, {master_node}

    max_time = 0

    while queue:
        current = queue.popleft()
        current_time = visited[current]

        max_time = max(max_time, current_time)

        for neighbor in graph.get(current, []):
             
            if neighbor in offline_nodes:
                failed_subtrees.add(neighbor)
                continue

            
            if neighbor not in visited:
                visited[neighbor] = current_time + 1
                queue.append(neighbor)

    return max_time, visited, failed_subtrees

 
cdn_network = {
    "master": ["Reg1", "Reg2", "Reg3"],
    "Reg1": ["EdgeA", "EdgeB"],
    "Reg2": ["EdgeC"],
    "Reg3": ["EdgeD"],
    "EdgeA": ["EdgeD"],
    "EdgeB": [],
    "EdgeC": [],
    "EdgeD": []
}

 
offline = {"Reg2"}

 
total_time, reach_times, failed = invalidate_cdn_cache(
    cdn_network,
    "master",
    offline
)

 
print("Total time to propagate:", total_time, "seconds")
print("Node Invalidation Times:", reach_times)
print("Failed Subtree Roots:", failed)

SCENARIO 2

Problem Statement
Title: Safe Cave Exploration and Longest Path Mapping Using DFS

Description:

Simulate an autonomous rover exploring an underground cave system mapped as an undirected graph of interconnected chambers and tunnels. The rover uses Depth-First Search (DFS) to discover safe chambers, bypass hazardous areas (like gas pockets), and record the single longest continuous path it can travel without visiting a chamber twice.

Task
Build an undirected cave map where nodes represent chambers and edges represent tunnels.

Traverse the cave using DFS starting from the "Entrance".

Avoid entering any chamber listed in hazards.

Calculate:

Discovered Chambers: All safe chambers visited by the rover.

Longest Safe Path: The longest sequence of connected chambers explored in a single continuous branch.

Path Length: The total number of chambers in that longest path.

Example (Using Provided Data)
Tunnels: Entrance connects to Chamber A, Chamber B, Chamber C

Hazards: {"Gas pocket"}

class CaveRoverMapper:

    def __init__(self):
        self.graph = {}
        self.visited = set()
        self.longest_path = []

    def explore_cave_dfs(self, current_node, hazards, current_path):
        self.visited.add(current_node)
        current_path.append(current_node)
    
        if len(current_path) > len(self.longest_path):
            self.longest_path = list(current_path)

        for neighbor in self.graph.get(current_node, []):
          
            if neighbor in hazards:
                continue

            if neighbor not in self.visited:
                self.explore_cave_dfs(
                    neighbor,
                    hazards,
                    current_path
                )





        current_path.pop()

    def add_tunnel(self, u, v):
      
        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)


if __name__ == "__main__":

    rover = CaveRoverMapper()


    tunnels = [
        ("Entrance", "Chamber A"),
        ("Entrance", "Chamber B"),
        ("Entrance", "Chamber C"),
        ("Chamber B", "Chamber E"),
        ("Chamber A", "Gas pocket"),
        ("Chamber B", "Chamber D"),
        ("Chamber D", "Deep Cave")
    ]

    for u, v in tunnels:
        rover.add_tunnel(u, v)

    hazards = {"Gas pocket"}

    rover.explore_cave_dfs(
        "Entrance",
        hazards,
        []
    )

    print("Chambers discovered & explored:")
    print(rover.visited)

    print("Longest Safe Exploration Path:")
    print(" -> ".join(rover.longest_path))

    print("Longest Safe Exploration Rate:",
          len(rover.longest_path), "nodes")
