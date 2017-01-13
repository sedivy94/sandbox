class Node:
	def __init__(self, name, neighbors=[]):
		self.name = name
		self.neighbors = neighbors
	def add_neighbor(self, neighbor):
		if  isinstance(neighbor, Node):
			self.neighbors.append(neighbor)
		elif ininstance(neighbor, list):
			self.neighbors.extend(neighbor)
		else:
			print("Invalid argument. Object is not a Node or list of Nodes.")
		return
	def remove_neighbor(self, neighbor):
		if  isinstance(neighbor, str):
			self.neighbors = [x for x in self.neighbors if x.name != neighbor]
		elif ininstance(neighbor, list):
			self.neighbors = self.neighbors = [x for x in self.neighbors for y in neighbor if x != y]	
		else:
			print("Invalid argument. Object is not a string or list of strings.")
		return
	def rename(self, name):
		self.name = name

class Graph:
	def __init__(self):
		self.node_set = set()
		self.lookup = dict()
	def add_node(self, node, neighbors=[]):
		if isinstance(node, str):
			new_node = Node(node, neighbors)
		elif isinstance(node, Node):
			new_node = node
		node_set.add(new_node)
		lookup[new_node.name] = new_node
	def remove_node(self, node):
		if isinstance(node, str):
			old_node = lookup[node]
			node_set.remove(old_node)
			lookup[node] = None
		elif isinstance(node, Node):
			node_set.remove(node)
			lookup[node.name] = None
		