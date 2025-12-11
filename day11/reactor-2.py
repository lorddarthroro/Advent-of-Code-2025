# this code augments the DFS algorithm from geeks for geeks https://www.geeksforgeeks.org/python/python-program-for-depth-first-search-or-dfs-for-a-graph/

def DFSUtil(v, visited, graph):

    if v == 'out':
        if 'dac' in visited and 'fft' in visited:
            return 1
        else:
            return 0
    
    visited.add(v)
    total_paths = 0

    for neighbour in graph[v]:
        if neighbour not in visited:
            total_paths += DFSUtil(neighbour, visited, graph)
    visited.remove(v)
    return total_paths

def DFS(v, graph):

    visited = set()

    return DFSUtil(v, visited, graph)

graph = {}

with open('advent-of-code-2025/day-11/data/input0-2.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue  
        
        name, outputs = line.split(":")
        name = name.strip()
        outputs = outputs.strip().split()
        
        graph[name] = outputs

print(DFS('svr', graph))

