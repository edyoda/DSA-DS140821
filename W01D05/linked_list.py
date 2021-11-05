class node():
	def __init__(self,data,link=None):
		self.data = data
		self.link = link

class LinkedList():
	def __init__(self):
		self.head = None

	def is_empty(self):
		if self.head == None:
			return True

	def append(self,value):
		new_node = node(value)
		if self.is_empty():
			self.head = new_node
		else:
			temp = self.head
			while temp.link != None:
				temp = temp.link
			temp.link = new_node
		print('Node have been inserted')

	def printList(self):
		temp = self.head
		while temp.link!= None:
			print(temp.data)
			temp = temp.link
		print(temp.data)

rohitsLinkedList = LinkedList()
rohitsLinkedList.append(100)
rohitsLinkedList.append(200)
rohitsLinkedList.append(300)
rohitsLinkedList.append(400)
rohitsLinkedList.append(500)
rohitsLinkedList.append(600)
rohitsLinkedList.printList()

TalibsLinkedList = LinkedList()
TalibsLinkedList.append(700)
TalibsLinkedList.append(500)
TalibsLinkedList.append(300)
TalibsLinkedList.append(100)
TalibsLinkedList.printList()