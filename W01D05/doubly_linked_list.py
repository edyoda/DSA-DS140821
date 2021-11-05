class node():
	def __init__(self,data,prev=None,nexti=None):
		self.data = data
		self.prev = prev
		self.nexti = nexti

class doubly():
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def append(self,value):
		new_node = node(value)
		if self.isEmpty():
			self.head = new_node
		else:
			temp = self.head
			while temp.nexti != None:
				temp = temp.nexti
			new_node.prev = temp
			temp.nexti = new_node

	def printList(self):
		temp = self.head
		while temp.nexti!= None:
			print(temp.data)
			temp = temp.nexti
		print(temp.data)


dll = doubly()
dll.append(100)
dll.append(200)
dll.append(300)
dll.append(400)
dll.append(500)
dll.append(600)
dll.append(700)

dll.printList()
