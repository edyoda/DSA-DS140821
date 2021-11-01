class array:
	def __init__(self, len):
		self.final_size = len
		self.length = 0
		self.data = []

	def add(self,element):
		if self.final_size > self.length:
			self.data.append(element)
			self.length += 1
			print('Added',element)
		else:
			print('Array is Full')

	def deleteAt(self,index):
		for i in range(index,self.length-1):
			self.data[i] = self.data[i+1]
		del self.data[self.length-1]
		self.length -= 1

	def insertAt(self,index,item):
		if self.final_size > self.length:
			for i in range(self.length,index,-1):
				self.data[i] = self.data[i-1]
			self.data[index] = item
			self.length += 1
		else:
			print('Array size is full')

array_obj = array(5)
array_obj.add(1)
array_obj.add(2)
array_obj.add(3)
array_obj.add(4)
array_obj.add(5)
array_obj.deleteAt(0)
array_obj.deleteAt(0)
array_obj.add(6)
array_obj.add(7)


