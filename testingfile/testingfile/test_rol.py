

# # test = ["spam", "spamq", "spamq", "spamq", "spama", "spam"]

# # def counter(arrlist):
# #     result = []
# #     for item in test:
# #         result.append('"{}"'':''"{}"'.format(item, test.count(item)))
# #     i = 0
# #     for item in result:
# #         if item == result[i]:
# #             result.pop(0)
# #             i += 1

# #     return result

# # print(counter(test))

# # def counter(x=1, y=2):
# #     if y > x:
# #         return x+y


# # print(counter(2, 15))

# #------------------------------------------------------------------------------#
# # A Linked List Node
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next_ = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, new_data):
#         # 1. Create a new node
#         # 2. Put in the data
#         # 3. Set next as None
#         new_node = Node(new_data)
#         # 4. If the Linked List is empty, then make the
#         # new node as head
#         if self.head is None:
#             self.head = new_node
#             return
#         # 5. Else traverse till the last node
#         last = self.head
#         while (last.next_):
#             last = last.next_
#         # 6. Change the next of last node
#         last.next_ = new_node
    
#     def reverse(self):
#         prev = None
#         current = self.head
#         while(current is not None):
#             next = current.next_
#             current.next_ = prev 
#             prev = current
#             current = next
#         self.head = prev
#         while (self.head):
#             yield self.head.data
#             self.head = self.head.next_


# if __name__ == "__main__":
#     ll1 = LinkedList()
#     for _ in range(1,21):
#         ll1.append(_)
    
# for _ in ll1.reverse():
#     print(_)


