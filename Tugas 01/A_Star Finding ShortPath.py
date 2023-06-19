import heapq

def a_star(graph, start, goal, sld):
    queue = [(0, start)]
    visited = set()

    while queue:
        (cost, current_node) = heapq.heappop(queue)
        if current_node == goal:
            return cost
        if current_node not in visited:
            visited.add(current_node)
            for nbor, distance in graph[current_node].items():
                if nbor not in visited:
                    heuristic_cost = sld[nbor]
                    heapq.heappush(queue,(cost + distance + heuristic_cost, nbor))

    return float('inf')

graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'G': 1, 'E': 3, 'C': 2},
    'C': {'E': 7, 'D': 7},
    'D': {'A': 2, 'F': 6},
    'E': {'D': 2, 'F': 1},
    'F': {},
    'G': {'E': 1}
}

sld = {
    'A': 9,
    'B': 7,
    'C': 0,
    'D': 6,
    'E': 5,
    'F': 2,
    'G': 0
}

start = 'A'
goal = 'G'
result = a_star(graph, start, goal, sld)
print(f'Jarak terpendek {start} ke {goal} = {result}.')