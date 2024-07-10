mahasiswa = []

while True:
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    
    mahasiswa.append({"NIM": nim, "Nama": nama})
    
    tambah_lagi = input("Ingin tambah lagi? (ya/tidak): ")
    if tambah_lagi.lower() != 'ya':
        break

print("Data Mahasiswa:")
for data in mahasiswa:
    print(f"NIM: {data['NIM']}, Nama: {data['Nama']}")
