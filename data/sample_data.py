
from models.node import Node
from structures.organization_tree import OrganizationTree


def buat_data_organisasi():

    root = Node("RKT-001", "Rektor", "Rektor (Root)")

    root.tambah_bawahan(
        Node("SNT-001", "Senat Universitas", "Senat Universitas")
    )

    root.tambah_bawahan(
        Node("WR1-001", "Wakil Rektor I",
             "Wakil Rektor I (Bidang Akademik)")
    )

    root.tambah_bawahan(
        Node("WR2-001", "Wakil Rektor II",
             "Wakil Rektor II (Bidang Administrasi Umum & Keuangan)")
    )

    root.tambah_bawahan(
        Node("WR3-001", "Wakil Rektor III",
             "Wakil Rektor III (Bidang Kemahasiswaan & Kerja Sama)")
    )

    dekan = Node(
        "DKN-001",
        "Dekan",
        "Dekan Fakultas Sains dan Teknologi"
    )

    root.tambah_bawahan(dekan)

    dekan.tambah_bawahan(
        Node("WD1-001", "Wakil Dekan I",
             "Wakil Dekan I (Bidang Akademik & Kelembagaan)")
    )

    dekan.tambah_bawahan(
        Node("WD2-001", "Wakil Dekan II",
             "Wakil Dekan II (Bidang AUPK)")
    )

    dekan.tambah_bawahan(
        Node("WD3-001", "Wakil Dekan III",
             "Wakil Dekan III (Bidang Kemahasiswaan)")
    )

    kaprodi = Node(
        "KPR-001",
        "Ketua Program Studi",
        "Ketua Program Studi Teknik Informatika"
    )

    dekan.tambah_bawahan(kaprodi)

    kaprodi.tambah_bawahan(
        Node("SPR-001", "Sekretaris Program Studi",
             "Sekretaris Program Studi")
    )

    kalab = Node(
        "KLB-001",
        "Kepala Laboratorium",
        "Kepala Laboratorium Komputer"
    )

    kaprodi.tambah_bawahan(kalab)

    kalab.tambah_bawahan(
        Node("ASL-001", "Asisten Laboratorium",
             "Asisten Laboratorium")
    )

    kalab.tambah_bawahan(
        Node("TKS-001", "Teknisi Laboratorium",
             "Teknisi Laboratorium")
    )

    koordinator = Node(
        "KDS-001",
        "Koordinator Dosen",
        "Koordinator Dosen"
    )

    kaprodi.tambah_bawahan(koordinator)

    dosen_pa = Node(
        "DPA-001",
        "Dosen Pembimbing Akademik",
        "Dosen Pembimbing Akademik"
    )

    koordinator.tambah_bawahan(dosen_pa)

    dosen_pa.tambah_bawahan(
        Node("MHS-001", "Mahasiswa Bimbingan",
             "Mahasiswa Bimbingan (Leaf)")
    )

    koordinator.tambah_bawahan(
        Node("DPM-001", "Dosen Pengampu Mata Kuliah",
             "Dosen Pengampu Mata Kuliah")
    )

    return OrganizationTree(root)
