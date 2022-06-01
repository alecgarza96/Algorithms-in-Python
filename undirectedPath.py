def undirectedPath(edges, nodeA, nodeB):
      graph = buildGraph(edges)
      visited = set()
      return hasPath(graph, nodeA, nodeB, visited)

def hasPath(graph, src, dst, visited):
      if src in visited:
            return False
      if src == dst:
            return True
      visited.add(src)
      for neighbor in graph[src]:
            if hasPath(graph, neighbor, dst, visited) == True:
                  return True

      return False

def buildGraph(edges):
      graph = {}
      for edge in edges:
            [a,b] = edge
            if a not in graph:
                  graph[a] = []
            if b not in graph:
                  graph[b] = []
            graph[a].append(b)
            graph[b].append(a)
      return graph 


edges = [
      ['i','j'],
      ['k','i'],
      ['m','n'],
      ['k','l'],
      ['o','n']
]

print(buildGraph(edges))

print(undirectedPath(edges, 'i', 'j'))
