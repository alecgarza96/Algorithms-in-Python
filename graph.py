class Graph(object):
	def __init__(self, graph_dict=None):
		"""
		Initializes a graph object
		If no dictionary or None is given
		an empty dictionary will be used
		"""

		if graph_dict == None:
			graph_dict = {}
		self._graph_dict = graph_dict

	def edges(self, vertice):
		"""returns a list of all the edges of a vertice"""
		return self._graph_dict[vertice]

	def all_vertices(self):
		"""returns the vertices of a graph as a set"""
		return set(self._graph_dict.keys())

	def all_edges(self):
		"""returns the edges of a graph"""
		return self.__generate_edges()

	def add_vertex(self, vertex):
		if vertex not in self._graph_dict:
			self._graph_dict[vertex] = []

	def add_edge(self, edge):
		edge = set(edge)
		vertex1, vertex2 = tuple(edge)
		for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
			if x in self._graph_dict:
				self._graph_dict[x].add(y)
			else:
				self._graph_dict[x] = [y]

	def __generate_edges(self):
		edges = []
		for vertex in self._graph_dict:
			for neighbour in self._graph_dict[vertex]:
				if {neighbour, vertex} not in edges:
					edges.append({vertex, neighbour})
		return edges

	def __iter__(self):
		self._iter_obj = iter(self._graph_dict)
		return self._iter_obj

	def __next__(self):
		return next(self._iter_obj)

	def __str__(self):
		res = "vertices: "
		for k in self._graph_dict:
			res += str(k)+" "
		res += "\nedges: "
		for edge in self.__generate_edges():
			res += str(edge)+" "
		return res

	def find_path(self, start_vertex, end_vertex, path=None):
		if path == None:
			path = []
		graph = self._graph_dict
		path = path + [start_vertex]
		if start_vertex == end_vertex:
			return path
		if start_vertex not in graph:
			return None
		for vertex in graph[start_vertex]:
			if vertex not in path:
				extended_path = self.find_path(vertex, end_vertex, path)
				if extended_path:
					return extended_path
		return None

	def find_all_paths(self, start_vertex, end_vertex, path=[]):
		graph = self._graph_dict
		path = path + [start_vertex]
		if start_vertex == end_vertex:
			return [path]
		if start_vertex not in graph:
			return []
		paths = []
		for vertex in graph[start_vertex]:
			if vertex not in path:
				extended_paths = self.find_all_paths(vertex, end_vertex, path)
				for p in extended_paths:
					paths.append(p)
		return paths

g = { "a" : {"d"},
      "b" : {"c"},
      "c" : {"b", "c", "d", "e"},
      "d" : {"a", "c"},
      "e" : {"c"},
      "f" : {}
    }


graph = Graph(g)

print("Vertices of graph:")
print(graph.all_vertices())

print("Edges of graph:")
print(graph.all_edges())


print('The path from vertex "a" to vertex "b":')
path = graph.find_path("a", "b")
print(path)

print('The path from vertex "a" to vertex "f":')
path = graph.find_path("a", "f")
print(path)

print('The path from vertex "c" to vertex "c":')
path = graph.find_path("c", "c")
print(path)
