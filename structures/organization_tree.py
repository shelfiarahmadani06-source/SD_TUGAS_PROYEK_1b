
from models.node import Node


class OrganizationTree:
    """Implementasi General Tree untuk hierarki organisasi."""

    def __init__(self, root):
        self.root = root

    def search_node(self, kata_kunci):
        """Mencari node berdasarkan ID, nama, atau jabatan."""
        if self.root is None:
            return None

        key = str(kata_kunci).casefold()
        stack = [self.root]

        while stack:
            node = stack.pop()

            if (key == node.id.casefold()
                    or key in node.nama.casefold()
                    or key in node.jabatan.casefold()):
                return node

            stack.extend(reversed(node.children))

        return None

    def search_node_by_id(self, id):
        """Mencari node berdasarkan ID yang sama persis."""
        if self.root is None:
            return None

        stack = [self.root]

        while stack:
            node = stack.pop()

            if node.id == id:
                return node

            stack.extend(reversed(node.children))

        return None

    def insert_node(self, id, nama, jabatan, atasan):
        """Menyisipkan pegawai baru di bawah atasan tertentu."""

        atasan_node = self.search_node(atasan)

        if atasan_node is None:
            return False

        if self.search_node_by_id(id) is not None:
            return False

        node_baru = Node(id, nama, jabatan)

        atasan_node.tambah_bawahan(node_baru)

        return True

    def preorder(self, node=None):
        """Root -> Children."""

        if node is None:
            node = self.root

        if node is None:
            return []

        hasil = [node.jabatan]

        for anak in node.children:
            hasil.extend(self.preorder(anak))

        return hasil

    def inorder(self, node=None):
        """Konvensi General Tree: anak pertama -> node -> anak berikutnya."""

        if node is None:
            node = self.root

        if node is None:
            return []

        hasil = []

        if node.children:
            hasil.extend(self.inorder(node.children[0]))

        hasil.append(node.jabatan)

        for anak in node.children[1:]:
            hasil.extend(self.inorder(anak))

        return hasil

    def postorder(self, node=None):
        """Children -> Root."""

        if node is None:
            node = self.root

        if node is None:
            return []

        hasil = []

        for anak in node.children:
            hasil.extend(self.postorder(anak))

        hasil.append(node.jabatan)

        return hasil

    def tampilkan_struktur(self, node=None, level=0):
        """Menampilkan hierarki organisasi."""

        if node is None:
            node = self.root

        if node is None:
            return

        print("    " * level + f"- {node.jabatan} [ID: {node.id}]")

        for anak in node.children:
            self.tampilkan_struktur(anak, level + 1)
