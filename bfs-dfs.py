from collections import defaultdict

# Recursive Breadth-First Search (BFS)
def bfs_recursive(graph, start, visited=None, queue=None):
    if visited is None:
        visited = set()
    if queue is None:
        queue = []
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

    if queue:
        bfs_recursive(graph, queue.pop(0), visited, queue)

# Recursive Depth-First Search (DFS)
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)




# Take user input to create the graph
graph = defaultdict(list)
num_vertices = int(input("Enter the number of vertices: "))

for i in range(num_vertices):
    neighbors = input(f"Enter the neighbors of vertex {i}: ").split()
    graph[i] = [int(neighbor) for neighbor in neighbors]

start_vertex = int(input("Enter the starting vertex: "))

print("BFS (Recursive):")
bfs_recursive(graph, start_vertex)
print("\nDFS (Recursive):")
dfs_recursive(graph, start_vertex)
