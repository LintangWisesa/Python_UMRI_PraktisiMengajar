
# show 1-10000, tapi jika sampai di 9998 tolong stop
for i in range(1,10001,1):
    print(i)
    if i == 9998:
        break

# show 1-10000, tapi tolong skip 9998
for i in range(1,10001,1):
    if i == 9998:
        continue
    print(i)

# Coba buat script python untuk menghitung 
# MEAN, MEDIAN, MODUS dari sebuah list numeric
x = [1, 2, 4, 5, 12, 1, 99, 120, 6, 5, 8, 45]