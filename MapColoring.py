from typing import Dict, List

def constraints(node: str, color: str, assignment: Dict[str, str], graph: Dict[str, List[str]]) -> bool:
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment: Dict[str, str], graph: Dict[str, List[str]],
              domain: Dict[str, List[str]]) -> Dict[str, str]:
    if len(assignment) == len(graph):
        return assignment
    node = None
    for n in graph:
        if n not in assignment:
            node = n
            break

    for value in domain[node]:
        if constraints(node, value, assignment, graph):
            assignment[node] = value
            result = backtrack(assignment, graph, domain)
            if result is not None:
                return result
            del assignment[node]
    return None


def map_coloring(graph: Dict[str, List[str]], colors: List[str]) -> Dict[str, str]:
    domain = {node: colors for node in graph}
    return backtrack({}, graph, domain)

graph = {
    'WA':  ['NT', 'SA'],
    'NT':  ['WA', 'SA', 'Q'],
    'SA':  ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q':   ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V':   ['SA', 'NSW'],
    'T':   ['V']
}
colors = ['red', 'green', 'blue']
solution = map_coloring(graph, colors)
print(solution)