from Soal_3 import RestoranTegal

restoran = RestoranTegal()

while True:
    print("\nMenu:")
    print("1. Tambah Pesanan")
    print("2. Hapus Pesanan")
    print("3. Tampilkan Antrian")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == '1':
        pesanan = input("Masukkan pesanan: ")
        restoran.enqueue(pesanan)
    elif pilihan == '2':
        restoran.dequeue()
    elif pilihan == '3':
        restoran.tampilkan_antrian()
    elif pilihan == '4':
        print("Terima kasih telah menggunakan sistem antrian Restoran Tegal.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

