# SET: himpunan, python collection, not indexed, immutable, not allow duplicate

x = {1, 2, 3, 4, 5}
print(x)
# print(x[0])         # TypeError: 'set' object is not subscriptable
# x[0] = 100
# print(x)            # TypeError: 'set' object does not support item assignment

x.add(6)            # add angka 6
print(x)
x.remove(2)         # hapus angka 2
print(x)
x.discard(1)        # hapus angka 1
print(x)
# remove: jika element yg akan diremove tidak exist di dalam set => ERROR
# discard: jika element yg akan diremove tidak exist di dalam set => NOT ERROR

# x.clear()             # hapus all elements
# del x                 # hapus variabel x

# set methods
asli = {1, 2, 3, 4, 5}
ganjil = {1, 3, 5, 7, 9}
genap = {2, 4, 6, 8, 10}

# UNION
print(asli.union(ganjil))           # UNION dari asli & ganjil = 1, 2, 3, 4, 5, 7, 9
print(asli.union(ganjil, genap))    # UNION: all elements from all sets = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(asli | ganjil | genap)

# INTERSECTION / IRISAN
print(asli.intersection(ganjil))        # irisan dari asli & ganjil = 1, 3, 5
print(asli.intersection(ganjil, genap)) # irisan dari 3 set = {}
print(asli & ganjil)

# DIFFERENTIATE / SELISIH
print(asli.difference(genap))   # cari elemen berbeda di asli, tp tidak ada di genap
print(genap.difference(asli))   # cari elemen berbeda di genap, tp tidak ada di asli
print(asli - genap)
print(genap - asli)