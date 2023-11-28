# built-in higher order functions
# 1. lambda
def a():
    return 28
x = lambda a: a
print(x(12))
print(x(a()))

# 2. map(func, iter): menerapkan suatu func ke setiap elemen sequence iter
angka = [2, 6, 10, 11, 13, 15, 22, 24]
# buat list yg mengandung kuadrat dari tiap elemen pada list angka
# [2, 6, 10, 11] => [4, 36, 100, 121]
def pangkatDua(i):
    return i ** 2
kuadrat = list(map(pangkatDua, angka))
print(kuadrat)

# 3. filter(func, iter): menerapkan data filtering dg requirement: func ke tiap elemen dlm sequence
# buat list yg hasil filter berupa angka genap saja dari list angka
def filterGenap(i):
    if i % 2 == 0:
        return True
    else:
        return False
genapAja = list(filter(filterGenap, angka))
print(genapAja)
