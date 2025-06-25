def BFS_iterative(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop()
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(reversed(graph[node]))
graph = {
    'A':['B', 'C'],
    'B':['D'],
    'C':['E'],
    'D':[],
    'E':[]
}
BFS_iterative(graph,'A')