
from data.sample_data import buat_data_organisasi
from views.cli import jalankan_aplikasi


def main():

    organisasi = buat_data_organisasi()

    jalankan_aplikasi(organisasi)


if __name__ == "__main__":
    main()
