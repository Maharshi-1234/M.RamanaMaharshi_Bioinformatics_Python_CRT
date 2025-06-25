def bfs_recursive(graph, current_level, visited):
    if not current_level:
        return
    next_level = []
    for node in current_level:
        if node not in visited:
            print(node)
            visited.add(node)
            next_level.extend(graph[node])
    bfs_recursive(graph, next_level, visited)
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}
visited = set()
bfs_recursive(graph, ['A'], visited)
