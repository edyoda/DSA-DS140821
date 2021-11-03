class Stack():
	def __init__(self):
		self.data = []

	def push(self,item):
		self.data.append(item)

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
expression = input()
for char in expression:
	if char in ['{','[','(']:
		stack_obj.push(char)
	else:
		if stack_obj.size() == 0:
			print('Expression is not Balanced!')
			break
		if char == '}':
			if stack_obj.peek() == '{':
				stack_obj.pop()
			else:
				print('Expression is not Balanced!')
				break
		if char == ')':
			if stack_obj.peek() == '(':
				stack_obj.pop()
			else:
				print('Expression is not Balanced!')
				break
		if char == ']':
			if stack_obj.peek() == '[':
				stack_obj.pop()
			else:
				print('Expression is not Balanced!')
				break
else:
	if stack_obj.isEmpty():
		print('Expression is Balanced')
	else:
		print('Expression is not Balanced!')