
import unittest

from data.sample_data import buat_data_organisasi


class TestOrganizationTree(unittest.TestCase):

    def setUp(self):
        self.tree = buat_data_organisasi()

    def test_search_existing_node(self):
        hasil = self.tree.search_node("Dekan")

        self.assertEqual(hasil.id, "DKN-001")

    def test_search_missing_node(self):
        hasil = self.tree.search_node("Jabatan Tidak Ada")

        self.assertIsNone(hasil)

    def test_insert_node(self):
        berhasil = self.tree.insert_node(
            "STF-TEST",
            "Budi",
            "Staf Administrasi",
            "Sekretaris Program Studi"
        )

        self.assertTrue(berhasil)

        hasil = self.tree.search_node_by_id("STF-TEST")

        self.assertIsNotNone(hasil)

    def test_duplicate_id_is_rejected(self):
        berhasil = self.tree.insert_node(
            "RKT-001",
            "Duplikat",
            "Jabatan Duplikat",
            "Rektor"
        )

        self.assertFalse(berhasil)

    def test_all_traversals_visit_18_nodes(self):

        self.assertEqual(len(self.tree.preorder()), 18)

        self.assertEqual(len(self.tree.inorder()), 18)

        self.assertEqual(len(self.tree.postorder()), 18)


if __name__ == "__main__":
    unittest.main()
