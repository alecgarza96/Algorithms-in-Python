def largestComponent(graph):
	visited = set()
	longest = 0
	for node in graph:
		size = exploreSize(graph, node, visited)
		if size > longest:
			longest = size
	return longest

def exploreSize(graph, node, visited):
	if visited.has(node):
		return 0

	visited.add(node)

	size = 1
	for neighbor in graph[node]:
		size += exploreSize(graph, neighbor, visited)

	return size





