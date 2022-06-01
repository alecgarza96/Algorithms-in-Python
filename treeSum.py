class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def depthFirstTreeSum(root):
	if root == None:
		return 0
	return root.val + depthFirstTreeSum(root.left) + depthFirstTreeSum(root.right)

def breadthFirstSum(root):
	if root == None:
		return 0
	queue = [root]
	totalSum = 0

	while len(queue) != 0:
		current = queue[0]
		queue = queue[1:]
		totalSum += current.val
		if current.left:
			queue.append(current.left)
		if current.right:
			queue.append(current.right)
	return totalSum

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(2)
e = Node(1)

a.left = b 
a.right = c 
b.left = d 
b.right = e 

print(depthFirstTreeSum(a))
print(breadthFirstSum(a))
