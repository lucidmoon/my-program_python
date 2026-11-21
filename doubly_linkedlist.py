# ===================
# Doubly Linked List
# ===================
class DNode:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None

class DoubleLinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = DNode(data)
    new_node.next = self.head
    if self.head:
      self.head.prev = new_node
    self.head = new.node

  def insert_at_end(self, data):
    new_node = DNode(data)
    if self.head is None:
      self.head = new_node
      return
    temp = self.head
    while temp.next:
      temp = temp.next
    temp.next = new_node
    new_node.prev = temp

  def delete_node(self, key):
    current = self.head
    while current:
      if current.data == key:
        if current.prev:
          current.prev.next = current.next
        else:
          self.head = current.next
        if current.next:
          current.next.prev = current.prev
        return
      current = current.next
  
  def traverse_forward(self):
    current = self.head
    while current:
      print(current.data, end=" <-> ")
      current = current.next
    print("None")

  def traverse_backward(self):
    current = self.head
    if not current:
      return
    # Arahkan ke node terakhir
    while current.next:
      current = current.next
    # Traversal mundur
    while current:
      print(current.data, end=" <-> ")
      current = current.prev
    print("None")

dll = DoubleLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)

print("Traversal Maju: ")
dll.traverse_forward()

print("Traversal Mundur: ")
dll.traverse_backward()

dll.delete_node(20)
print("Setelah Hapus 20: ")
dll.traverse_forward()
