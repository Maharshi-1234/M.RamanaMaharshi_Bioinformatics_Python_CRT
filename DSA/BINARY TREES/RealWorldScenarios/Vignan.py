## ◇ Scenario 1: Vignan Campus Map
'''
Context: Each building in a college campus is a node, and walkable paths are edges.
- Represent the campus map using an adjacency list.
- Check if there's a path from the Library to the Auditorium using BFS.
- List all buildings that are directly connected to the Admin Block.
- Use DFS to visit all reachable buildings from the Main Gate.
- Find if there are any disconnected buildings (buildings not connected to campus).
'''

campus = {
    "Main Gate": ["Admin Block"],
    "Admin Block": ["Main Gate", "Library", "Canteen", "Engineering Block"],
    "Library": ["Admin Block", "Auditorium"],
    "Canteen": ["Admin Block", "Hostel"],
    "Auditorium": ["Library"],
    "Engineering Block": ["Admin Block", "Science Block"],
    "Science Block": ["Engineering Block"],
    "Hostel": ["Canteen"]
}

def bfs(start, target):
    visited = set()
    queue = [start]
    while queue:
        b = queue.pop(0)
        if b == target:
            return True
        if b not in visited:
            visited.add(b)
            queue += [n for n in campus[b] if n not in visited]
    return False

def dfs(start, visited=None):
    if visited is None:
        visited = set()
    if start in visited:
        return
    print(start, end=' ')
    visited.add(start)
    for neighbor in campus[start]:
        dfs(neighbor, visited)
    return visited

def disconnected():
    visited = dfs("Main Gate", set())
    return set(campus.keys()) - visited

# 1. Adjacency List
print("1. Campus Map (Adjacency List):")
for b, n in campus.items():
    print(f"{b}: {n}")

# 2. Path from Library to Auditorium
print("\n2. Is there a path from Library to Auditorium?")
print("Yes" if bfs("Library", "Auditorium") else "No")

# 3. Directly connected buildings to Admin Block
print("\n3. Buildings directly connected to Admin Block:")
print(campus["Admin Block"])

# 4. DFS from Main Gate
print("\n4. DFS from Main Gate:")
dfs("Main Gate")

# 5. Disconnected buildings
print("\n\n5. Campus is Fully Connected!")
print(disconnected())
