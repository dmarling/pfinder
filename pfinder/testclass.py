class inventory(object):

	def __init__(self,name,capacity):
		self.name=name
		self.capacity=capacity
		self.itemlist=[]

	def additem(self, name, weight):
		if self.capacity < weight:
			raise RuntimeError('Total weight greater than capacity')
		self.itemlist.append(name)
		self.capacity-=weight
		print(self.itemlist)

	def removeitem(self, name, weight):
		self.itemlist.remove(name)
		self.capacity+=weight
		print(self.itemlist)
		
'''I can create an object 'storage' that uses the inventory class and gains access to its methods by'''
storage=inventory('greater sack', 50)

'''Note that 'object' is a placeholder and the use of values:'greater sack' and 50 applies to __init__ name and capacity'''
'''self applies to the object name 'storage''''

storage.additem('apple',2)
storage.additem('25 apples',25) #<--- will raise an error
'''Note I can declare a self.variable and initialize it to whatever I want, while reusing it as a global-esque variable for all my methods'''
