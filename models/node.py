
class Node:
    """Simpul untuk menyimpan data pegawai/jabatan."""

    def __init__(self, id, nama, jabatan):
        self.id = id
        self.nama = nama
        self.jabatan = jabatan
        self.children = []

    def tambah_bawahan(self, node):
        self.children.append(node)
