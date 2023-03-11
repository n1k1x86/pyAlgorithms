"""
We have following graph:
    start: a - 6, b - 2;
    a: end - 1;
    b: a - 3, end - 5
"""

"""Graph creation via hash-tables(dictioraries)"""
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['end'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['end'] = 5

graph['end'] = {}

"""Creation hash-table with costs"""
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['end'] = infinity

"""Creation hash-table with node's parents"""
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['end'] = None

"""Creation a list with processed nodes"""
processed = []

def find_lowest_cost_node(costs: dict) -> str:
    lowest_cost = float('inf')
    lowest_cost_node = None
    for i in costs:
        cost = costs[i]
        if cost < lowest_cost and i not in processed:
            lowest_cost = cost
            lowest_cost_node = i
    return lowest_cost_node

node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)