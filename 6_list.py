# LIST: python collection, indexed, mutable, allow duplicates

angka = [1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 2, 10]
print(angka[0])         # akses elemen indeks ke-0 / elemen pertama
print(angka[3])         # akses elemen indeks ke-3
print(angka.index(10))  # angka 10 itu indeks ke berapa
print(angka[24])

# start:stop:step
print(angka[:5])         # akses elemen ke 0-4
print(angka[0:5])        # akses elemen ke 0-4
print(angka[0:5:2])      # akses elemen 0, 2, 4

buah = ["Apel", "Belimbing", "Ceri", "Duku"]
print(buah)
buah.append("Jambu")    # add element at the end
print(buah)
buah.insert(1, "Semangka")  # add element at certain index (index = 1)
buah.insert(3, "Melon")  # add element at certain index (index = 3)
print(buah)
buah.remove("Duku")     # remove Duku from the list
print(buah)
buah.pop()              # remove last element
buah.pop(0)             # remove element index - 0
print(buah)

buah.sort()             # sort ascending alphabetically / numerically 
print(buah)
buah.sort(reverse=True) # sort descending
print(buah)