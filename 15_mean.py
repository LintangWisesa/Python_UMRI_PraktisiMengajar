# MEAN: rata-rata nilai = jumlah semua elemen / total n elemen
x = [1, 2, 4, 5, 12, 1, 99, 120, 6, 5, 8, 45]

jumlahX = 0
for i in x:
    # jumlahX = jumlahX + i
    jumlahX += i
print(jumlahX)

jumlahX = sum(x)
print(jumlahX)

nX = len(x)
print(nX) 

mean = jumlahX / nX
print(mean)

