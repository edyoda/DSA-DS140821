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

	def delete(self,key):
		temp = self.head
		while temp.nexti.data != key:
			temp = temp.nexti
		# once we have reached the stage where the next node contains the data to be deleted, we can have the following references:-
		previous_node = temp
		node_to_be_deleted = previous_node.nexti
		next_node = node_to_be_deleted.nexti
		# Now update the previous and next node such that they connect directly leaving the node_to_be_deleted.
		previous_node.nexti = node_to_be_deleted.nexti
		next_node.prev = node_to_be_deleted.prev


dll = doubly()
dll.append(100)
dll.append(200)
dll.append(300)
dll.append(400)
dll.append(400)
dll.append(500)
dll.append(600)
dll.append(700)

dll.printList()
dll.delete(400)
print('Deleting success')
dll.printList()
