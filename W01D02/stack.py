class Stack():
	def __init__(self):
		self.data = []

	def push(self,item):
		self.data.append(item)
		print(item)

	def pop(self):
		if len(self.data) >= 1:
			self.data.pop()
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

stack_obj = Stack()

stack_obj.push('mango')
stack_obj.push('banana')
stack_obj.push('kiwi')
stack_obj.pop()
stack_obj.peek()
stack_obj.display()