# Python Collections
# - List: ada index, bisa dirubah elemennya, bisa ada duplikat elemen []
# - Tuple: ada index, TIDAK bisa dirubah elemennya, bisa ada duplikat elemen ()
# - Set: TIDAK ada index, TIDAK bisa dirubah elemennya, TIDAK bisa ada duplikat elemen {}
# - Dictionary: ada index (KEY), bisa dirubah elemennya, TIDAK bisa ada duplikat elemen {key: value}

listAngka = [1, 2, 3, 4, 5]
tupleAngka = (1, 2, 3, 4, 5)
setAngka = {1, 2, 3, 4, 5}
dictAngka = {"A": 1, "B": 2, "C": 3}

print(type(listAngka))
print(type(tupleAngka))
print(type(setAngka))
print(type(dictAngka))

print(listAngka[0])
print(listAngka[-1])
print(tupleAngka[0])
print(tupleAngka[-1])
print(dictAngka["B"])