data = {
    'Nama': ['Mahasiswa 1', 'Mahasiswa 2', 'Mahasiswa 3'],
    'Algoritma': [90, 50, 65],
    'Matematika': [80, 60, 70]
}

rata_algoritma = sum(data['Algoritma']) / len(data['Algoritma'])
rata_matematika = sum(data['Matematika']) / len(data['Matematika'])
print(f"Rata-rata Algoritma: {rata_algoritma}")
print(f"Rata-rata Matematika: {rata_matematika}")


for i in range(len(data['Nama'])):
    rata_mahasiswa = (data['Algoritma'][i] + data['Matematika'][i]) /2
    print(f"{data['Nama'][i]}: {rata_mahasiswa}")
