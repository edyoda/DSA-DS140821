class Queue:
	def __init__(self):
		self.data = []

	def enqueue(self, item):
		self.data.insert(0, item)

	def dequeue(self):
		self.data.pop()

	def size(self):
		return len(self.data)

	def isEmpty(self):
		return self.data == []

q = Queue()
q.enqueue('Mohit')
q.enqueue('Aditya Kumar')
q.enqueue('Mohammad Sadiq')
q.dequeue()
q.enqueue('Himanshu')
q.enqueue('Talib')
print(q.data)
