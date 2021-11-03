# Python program to reverse a
# linked list in group of given size

# Node class


class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	def reverse(self, k):
		if self.head is None:
			return
		curr = self.head
		prev = None
		new_stack = []
		while curr is not None:
			val = 0
			# Terminate the loop whichever comes first
			# either current == None or value >= k
			while curr is not None and val < k:
				new_stack.append(curr.data)
				curr = curr.next
				val += 1
			# Now pop the elements of stack one by one
			while new_stack:

				# If final list has not been started yet.
				if prev is None:
					prev = Node(new_stack.pop())
					self.head = prev
				else:
					prev.next = Node(new_stack.pop())
					prev = prev.next

		# Next of last element will point to None.
		prev.next = None
		return self.head

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Utility function to print the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next


# Driver program
llist = LinkedList()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("Given linked list")
llist.printList()
llist.head = llist.reverse( 3)

print("\nReversed Linked list")
llist.printList()

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
