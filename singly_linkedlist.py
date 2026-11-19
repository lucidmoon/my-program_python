# ===================
# Singly Linked List
# ===================
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class SingleLinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    current = self.head
    while current.next:
      current = current.next
    current.next = new_node

  def delete_node(self, key):
    current = self.head
    if current and current.data == key:
      self.head = current.next
      return
    prev = None
    while current and current.data != key:
      prev = current
      current = current.next
    if current is None:
      return
    prev.next = current.next

  def traverse(self):
    current = self.head
    while current:
      print(current.data, end=" -> ")
      current = current.next
    print("None")

sll = SingleLinkedList()
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_beginning(5)
sll.insert_at_end(30)

print("Isi linked list:")
sll.traverse()

sll.delete_node(20)
print("Setelah menghapus 20:")
sll.traverse()
