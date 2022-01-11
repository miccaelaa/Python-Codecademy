from blossom_lib import flower_definitions 
from linked_list import Node, LinkedList

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for number in range(self.array_size)]

  def hash(self, key):
    return sum(key.encode())
  
  def compress(self,hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for i in list_at_array:
      if key == i[0]:
        i[1] = value
        return
    list_at_array.insert(payload)

  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    for i in list_at_index:
      if key == i[0]:
        return i[1]
    return None

# TEST #
blossom = HashMap(len(flower_definitions))
# Assign the values to their keys
for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])
# Look up a flower's meaning
print(blossom.retrieve('daisy'))
print(blossom.retrieve('hyacinth'))

#Assign new values
print(blossom.retrieve('margarita'))
blossom.assign('margarita', 'love')
print(blossom.retrieve('margarita'))

    
