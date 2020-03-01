#Lab6 linked lists

from node.py import Node

class LinkedList:

	def __init__(self, size = 0, head = None, tail = None):

		self.size = size
		self.head = head
		self.tail = tail


	def getSize(self):
		return(self.size)

	def setSize(self, s):
			self.size = s 

	def getHead(self):
		return(self.size)

	def setHead(self, h):
			self.head = h

	def getTail(self):

		def setTail(self, t):
			self.Tail =  t

	def isEmpty(self):

		if(self.getSize() > 0):

			return(False)
		
		return(True)
	
	def addNode(self, d):
		newNode = Node(data = d)

		if(self.isEmpty()):
			self.setHead(newNode)
			self.setTail(newNode)
			self.setSize(size + 1)

		else:
			print("HERE")
			temp_tail = self.getTail()
			print(temp_tail.getData


		self.setTail(newNode)
		self.setSize(self.size + 1)

def main():

	ll = LinkedList()
	ll.addNode(1000)
	ll.addNode(2000)

	print(ll.getTail.getData())

	ll.addNode("The American Unoversity")

if __name__ == '__main__':
	main()









if __name__ == '__main__':
	main()