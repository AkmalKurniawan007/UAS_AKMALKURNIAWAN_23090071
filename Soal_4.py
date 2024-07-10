class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def setNama(self, nama):
        self.nama = nama

    def setRasa(self, rasa):
        self.rasa = rasa

    def setWarna(self, warna):
        self.warna = warna

    def information(self):
        return f"Nama: {self.nama}, Warna: {self.warna}, Rasa: {self.rasa}"

class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.vitamin = vitamin

    def setVitamin(self, vitamin):
        self.vitamin = vitamin

    def information(self):
        parent_info = super().information()
        return f"{parent_info}, Vitamin: {self.vitamin}"


mangga1 = Mangga("Mangga Harum Manis", "Hijau", "Manis", "Vitamin C")


print(mangga1.nama)
print(mangga1.warna)
print(mangga1.rasa)
print(mangga1.vitamin)

print(mangga1.information())


mangga1.setNama("Mangga Arumanis")
mangga1.setWarna("Kuning")
mangga1.setRasa("Manis dan Asam")
mangga1.setVitamin("Vitamin A dan C")

print(mangga1.information())
