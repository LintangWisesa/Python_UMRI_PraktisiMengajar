# MODUS: nilai yang frekuensi kemunculannya tinggi
x = [1, 2, 4, 5, 12, 1, 99, 6, 5, 8, 45, 120, 5, 120, 120, 120]
print(x)
y = list(set(x))
print(y)

count = []
for i in y:
    c = 0
    for j in x:
        if j == i:
            c += 1
    count.append(c)
print(count)
# [1, 2, 99, 4, 5, 6, 8, 12, 45, 120]
# [2, 1,  1, 1, 3, 1, 1,  1,  1,   1]

modus = y[count.index(max(count))]
print(modus)