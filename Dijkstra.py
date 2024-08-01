import heapq
from collections import defaultdict, namedtuple
from functools import reduce

Graph = namedtuple('Graph', ['edges', 'nodes'])
Edge = namedtuple('Edge', ['start', 'end', 'cost'])

def create_graph(edges):
    graph = defaultdict(list)
    for edge in edges:
        graph[edge.start].append((edge.cost, edge.end))
        graph[edge.end].append((edge.cost, edge.start))  
    return Graph(graph, set(reduce(lambda acc, edge: acc | {edge.start, edge.end}, edges, set())))

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor_distance, neighbor in graph.edges[current_node]:
            distance = current_distance + neighbor_distance

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

edges = [
    Edge('A', 'B', 1),
    Edge('B', 'C', 2),
    Edge('A', 'C', 4),
    Edge('C', 'D', 1),
    Edge('B', 'D', 5)
]

graph = create_graph(edges)

start_node = 'A'
distances = dijkstra(graph, start_node)

print(f"Distances from start node {start_node}:")
for node, distance in distances.items():
    print(f"Node {node}: {distance}")