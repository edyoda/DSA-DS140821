class max_stack():
	def __init__(self):
		self.primary_stack = []
		self.secondary_stack = []

	def push(self,item):
		self.primary_stack.append(item)
		if len(self.secondary_stack) >= 1:
			if self.secondary_stack[-1] <= item:
				self.secondary_stack.append(item)
		else:
			self.secondary_stack.append(item)

	def pop(self):
		if len(self.primary_stack) >= 1:
			popped_value = self.primary_stack.pop()
			if popped_value == self.secondary_stack[-1]:
				self.secondary_stack.pop()

	def max(self):
		if len(self.secondary_stack) >=1:
			return self.secondary_stack[-1]

obj = max_stack()

obj.push(1)
obj.push(0.5)
print('max is',obj.max())	
obj.push(6)	
print('max is',obj.max())
obj.push(5)	
obj.push(5)	
print('max is',obj.max())
obj.push(6)
print('max is',obj.max())
obj.pop()
obj.pop()
obj.pop()
print('max is',obj.max())
obj.pop()
print('max is',obj.max())




