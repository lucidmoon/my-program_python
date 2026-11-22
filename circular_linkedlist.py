# ===================
# Circular Linked List
# ===================
class CNode:
  def __init__(self, data):
    self.data = data
    self.next = None

class CircularLinkedList:
  def __init__(self):
    self.head = None

  def tambah_di_akhir(self, data):
    node_baru = CNode(data)
    if self.head is None:
      self.head = node_baru
      node_baru.next = self.head
    else:
      temp = self.head
      while temp.next != self.head:
        temp = temp.next
      temp.next = node_baru
      node_baru.next = self.head

  def tampilkan(self):
    if self.head is None:
      print("List kosong.")
      return
    temp = self.head
    while True:
      print(temp.data, end=' -> ')
      temp = temp.next
      if temp == self.head:
        break
    print("(kembali ke head)")


cll = CircularLinkedList()
cll.tambah_di_akhir(10)
cll.tambah_di_akhir(20)
cll.tambah_di_akhir(30)
cll.tampilkan()
