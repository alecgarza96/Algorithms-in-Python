class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def breadthFirstSearch(root, target):
	if root == None:
		return False
	queue = [root]
	valueFound = False

	while len(queue) != 0 and valueFound == False:
		current = queue[0]
		queue = queue[1:]
		if current.val == target:
			valueFound = True
		else:
			if current.left:
				queue.append(current.left)
			if current.right:
				queue.append(current.right)
	return valueFound

def depthFirstSearch(root,target):
	if root == None:
		return False
	if root.val == target:
		return True
	return depthFirstSearch(root.left, target) or depthFirstSearch(root.right, target)

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b 
a.right = c 
b.left = d 
b.right = e 
c.right = f 

print(breadthFirstSearch(a, 'f'))
print(depthFirstSearch(a,'g'))
