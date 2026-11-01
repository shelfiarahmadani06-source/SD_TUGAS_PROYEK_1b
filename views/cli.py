
def tampilkan_hasil(judul, hasil):

    print(f"\n{judul}")
    print(" -> ".join(hasil))


def jalankan_aplikasi(tree):

    print("=" * 62)
    print("APLIKASI SILSILAH ORGANISASI - GENERAL TREE")
    print("=" * 62)

    print("\nSTRUKTUR ORGANISASI:")
    tree.tampilkan_struktur()

    print("\nCONTOH PENCARIAN:")

    hasil = tree.search_node("Dekan")

    if hasil:
        print(
            f"Ditemukan: {hasil.nama} | "
            f"{hasil.jabatan} | ID: {hasil.id}"
        )
    else:
        print("Data tidak ditemukan.")

    print("\nCONTOH PENYISIPAN:")

    sukses = tree.insert_node(
        "STF-001",
        "Budi",
        "Staf Administrasi",
        "Sekretaris Program Studi"
    )

    print(
        "Penyisipan berhasil."
        if sukses else "Penyisipan gagal."
    )

    tampilkan_hasil(
        "PREORDER TRAVERSAL:",
        tree.preorder()
    )

    tampilkan_hasil(
        "INORDER TRAVERSAL (konvensi General Tree):",
        tree.inorder()
    )

    tampilkan_hasil(
        "POSTORDER TRAVERSAL:",
        tree.postorder()
    )
