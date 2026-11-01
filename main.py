
from data.sample_data import buat_data_organisasi
from views.cli import jalankan_aplikasi


def main():

    organisasi = buat_data_organisasi()

    print("=" * 65)
    print("PROYEK STRUKTUR DATA - SILSILAH ORGANISASI")
    print("IMPLEMENTASI GENERAL TREE MENGGUNAKAN PYTHON OOP")
    print("=" * 65)

    print("\n1. STRUKTUR ORGANISASI")
    organisasi.tampilkan_struktur()

    print("\n2. PREORDER TRAVERSAL")
    print(" -> ".join(organisasi.preorder()))

    print("\n3. INORDER TRAVERSAL")
    print("(Konvensi General Tree)")
    print(" -> ".join(organisasi.inorder()))

    print("\n4. POSTORDER TRAVERSAL")
    print(" -> ".join(organisasi.postorder()))

    print("\n5. OPERASI PENCARIAN")
    hasil = organisasi.search_node("Dekan")

    if hasil:
        print("Data ditemukan!")
        print("ID       :", hasil.id)
        print("Nama     :", hasil.nama)
        print("Jabatan  :", hasil.jabatan)
    else:
        print("Data tidak ditemukan.")

    print("\n6. OPERASI PENYISIPAN")

    berhasil = organisasi.insert_node(
        "STF-001",
        "Budi",
        "Staf Administrasi",
        "Sekretaris Program Studi"
    )

    if berhasil:
        print("Data pegawai berhasil ditambahkan!")
        print("Nama     : Budi")
        print("Jabatan  : Staf Administrasi")
        print("Atasan   : Sekretaris Program Studi")
    else:
        print("Penyisipan data gagal.")

    print("\n7. STRUKTUR SETELAH PENYISIPAN")
    organisasi.tampilkan_struktur()

    print("\n" + "=" * 65)
    print("PROGRAM SELESAI")
    print("=" * 65)


if __name__ == "__main__":
    main()
