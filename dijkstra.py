import sys
import heapq

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = [[] for _ in range(num_vertices)]

    def add_edge(self, source, destination, weight):
        self.adjacency_list[source].append((destination, weight))
        self.adjacency_list[destination].append((source, weight))

    def dijkstra(self, source):
        distances = [sys.maxsize] * self.num_vertices
        distances[source] = 0

        # Use a priority queue (min heap) to get the vertex with minimum distance
        priority_queue = [(0, source)]

        while priority_queue:
            dist, current_vertex = heapq.heappop(priority_queue)

            # Ignore if we have already found a shorter path to the current vertex
            if dist > distances[current_vertex]:
                continue

            for neighbor, edge_weight in self.adjacency_list[current_vertex]:
                distance = distances[current_vertex] + edge_weight

                # If we found a shorter path to the neighbor, update its distance
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# Take user input for the graph
num_vertices = int(input("Enter the number of vertices: "))
graph = Graph(num_vertices)

num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    source, destination, weight = map(int, input("Enter source, destination, and weight (space-separated): ").split())
    graph.add_edge(source, destination, weight)

source_vertex = int(input("Enter the source vertex: "))
shortest_distances = graph.dijkstra(source_vertex)

print("Shortest distances from vertex", source_vertex)
for i, distance in enumerate(shortest_distances):
    print("Vertex", i, ":", distance)
