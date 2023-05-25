def add_edge(graph, edge1, edge2):
    graph[edge1][edge2] = 1
    graph[edge2][edge1] = 1

def is_safe(vertex, color, graph, v, colors):
    for i in range(v):
        if graph[vertex][i] == 1 and colors[i] == color:
            return False
    return True

def graph_coloring(graph, m, v, colors, vertex=0):
    if vertex == v:
        return True
    for color in range(1, m + 1):
        if is_safe(vertex, color, graph, v, colors):
            colors[vertex] = color
            if graph_coloring(graph, m, v, colors, vertex + 1):
                return True
            colors[vertex] = 0
    return False

def graph_coloring_main(graph, m, v):
    colors = [0] * v
    if graph_coloring(graph, m, v, colors):
        print("Graph can be colored using", m, "colors.")
        print("Color assignments:", colors)
    else:
        print("Graph cannot be colored using", m, "colors.")

if __name__ == '__main__':
    v = int(input("Enter the number of vertices: "))
    e = int(input("Enter the number of edges: "))
    m = int(input("Enter the number of colors: "))

    graph = [[0] * v for _ in range(v)]

    print("Enter the edges (vertex1 vertex2):")
    for _ in range(e):
        edge1, edge2 = map(int, input().split())
        add_edge(graph, edge1, edge2)

    graph_coloring_main(graph, m, v)
