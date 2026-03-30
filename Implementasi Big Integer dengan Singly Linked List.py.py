# ==============================
# SINGLE LINKED LIST - PYTHON
# ==============================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Tambah di awal
    def tambah_awal(self, data):
        node_baru = Node(data)
        node_baru.next = self.head
        self.head = node_baru

    # Tambah di akhir
    def tambah_akhir(self, data):
        node_baru = Node(data)
        if self.head is None:
            self.head = node_baru
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node_baru

    # Hapus data
    def hapus(self, key):
        temp = self.head

        # jika head yang dihapus
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Data tidak ditemukan")
            return

        prev.next = temp.next
        temp = None

    # Tampilkan data
    def tampil(self):
        temp = self.head
        if temp is None:
            print("Linked list kosong")
            return

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ==============================
# PROGRAM UTAMA
# ==============================

ll = LinkedList()

ll.tambah_awal(10)
ll.tambah_awal(5)
ll.tambah_akhir(20)
ll.tambah_akhir(30)

print("Data setelah ditambahkan:")
ll.tampil()

ll.hapus(20)

print("Data setelah dihapus:")
ll.tampil()