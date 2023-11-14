# LIST: python collection, indexed, mutable, allow duplicates

angka = [1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 2, 10]
print(angka[0])         # akses elemen indeks ke-0 / elemen pertama
print(angka[3])         # akses elemen indeks ke-3
print(angka.index(10))  # angka 10 itu indeks ke berapa
print(angka[24])

# start:stop:step
print(angka[:5])         # akses elemen ke 0-4
print(angka[0:5])        # akses elemen ke 0-4
print(angka[0:5:1])      # akses elemen 0, 2, 4