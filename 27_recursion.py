# Concepts of Functional Programming
# 1. Pure functions
# 2. Recursion
# 3. Referential transparency
# 4. Functions are First-Class and can be Higher-Order

# Recursion
# di dalam func programming, tidak ada konsep looping: for loop & while loop
# recursion: func memanggil dirinya sendiri

# jumlah elemen2 dalam list
x = [1, 2, 3, 4, 5]
total = 0
for i in x:
    total = total + i
print(total) 

# recursion
def jumlah(listAngka):
    if len(listAngka) == 0:
        return 0
    elif len(listAngka) == 1:
        return listAngka[0]
    else:
        return listAngka[0] + jumlah(listAngka[1:])
print(jumlah(x))