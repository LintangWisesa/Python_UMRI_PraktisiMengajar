# TUPLE: python collection, indexed, immutable, allow duplicate

x = (1, 2, 3, 4, 5, 2)
print(x[0])     # akses elemen ke-0
print(x[4])     # akses elemen ke-4
print(x[-1])    # akses elemen ke-1 dari belakang aka terakhir
print(x[-2])    # akses elemen ke-2 dari belakang
print(x[0:5:2]) # dari 0-4 dengan step 2: indeks 0, 2, 4 = (1, 3, 5)
print(x[1:5:2]) # dari 1-4 dengan step 2: indeks 1, 3 = (2, 4)

# x[0] = 100      # TypeError: 'tuple' object does not support item assignment
# print(x)