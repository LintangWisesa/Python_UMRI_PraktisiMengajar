# inheritance: konsep pewarisan properti antar class

# parent class
class Person:
    def __init__(self, name, city):
        self.nama = name
        self.kota = city
    def hello(self):
        return "Hi I'm " + self.nama + " from " + self.kota

# child class inheritance terhadap parent class
class People(Person):
    pass    # objek yg terbentuk dari People akan identik dg objek yg terbentuk dari Person
    
# child class Mahasiswa, inherit thd People + additional property: kampus & nim
class Mahasiswa(People):
    def __init__(self, name, city, univ, id):
        People.__init__(self, name, city)
        self.kampus = univ
        self.nim = id

# child class Dosen, inherit thd People + additional property: kampus & nip
class Dosen(People):
    def __init__(self, name, city, univ, id):
        super().__init__(name, city)
        self.kampus = univ
        self.nip = id

andi = Mahasiswa("Andi", "Jakarta", "UMRI", 12345)
print(andi.nama)
print(andi.kota)
print(andi.kampus)
print(andi.nim)
print(andi.hello())

budi = Dosen("Budi", "Bandung", "UMRI", 54321)
print(budi.nama)
print(budi.kota)
print(budi.kampus)
print(budi.nip)
print(budi.hello())