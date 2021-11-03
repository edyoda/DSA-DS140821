class Stack():
	def __init__(self):
		self.data = []

	def push(self,item):
		self.data.append(item)

	def pop(self):
		if len(self.data) >= 1:
			return self.data.pop()
		else:
			print('Noting to Pop')

	def peek(self):
		if len(self.data) >= 1:
			return self.data[-1]
		else:
			print('Noting to Peek')

	def isEmpty(self):
		return not bool(len(self.data))

	def size(self):
		return len(self.data)

	def display(self):
		print('Printing from bottom to top')
		for i in self.data:
			print(i)

class Queue_from_Stacks():
	def __init__(self):
		self.prime = Stack()
		self.second = Stack()

	def enqueue(self, item):
		if self.prime.isEmpty():
			self.prime.push(item)
		else:
			while not self.prime.isEmpty():
				popped_item = self.prime.pop()
				self.second.push(popped_item)
			self.prime.push(item)
			while not self.second.isEmpty():
				popped_item = self.second.pop()
				self.prime.push(popped_item)

	def dequeue(self):
		if self.prime.isEmpty():
			print('Empty Queue')
		else:
			self.prime.pop()


q = Queue_from_Stacks()
q.enqueue('Mohit')
q.enqueue('Aditya Kumar')
q.enqueue('Mohammad Sadiq')
q.dequeue()
q.enqueue('Himanshu')
q.enqueue('Talib')
q.prime.display()
q.dequeue()
q.prime.display()