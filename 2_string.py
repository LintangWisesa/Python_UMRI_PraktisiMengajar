# String: textual data type, use "..." / '...'
firstName = "Ali"
lastName = 'Wirawan'
print(firstName, lastName)
print(f"Hi I'm {firstName} {lastName}")

# multiline string, triple double quote """...""" / triple single quote '''...'''
sentence = """
    Lorem ipsum bla bla bla
    Test 1 2 3
    OK
"""
sentence2 = '''
    Tes 123
    Tes 456
'''
print(sentence)
print(sentence2)

# string = array, collection of characters
x = 'Indonesia'
print(x[0]) # akses x elemen index ke-0 a.k.a karakter ke-1
print(x[4]) # akses x elemen index ke-4 a.k.a karakter ke-5
print(x[8]) # akses x elemen index ke-8 a.k.a karakter ke-9
print(len(x))           # panjang karakter x, berapa karakter? 9
print(x[len(x)-1])      # akses elemen terakhir: index elemen terakhir = 9 - 1
print(x[-1])            # akses elemen terakhir
print(x[-2])            # akses elemen ke-2 dari belakang

# ambil kata "done" dari "Indonesia"
print(x[2])
print(x[5])
print(x[2:6])   # ambil index ke 2-6, tapi index 6 tidak diikutkan
print(x[5:])    # esia: ambil x dari elemen index ke-5 dst
print(x[:4])    # Indo: ambil x dari index 0-4, 4 tidak ikut
print(x[0:4])   # Indo: ambil x dari index 0-4, 4 tidak ikut

# x[start:stop:skip]
print(x[0::2])  # Idnsa
print(x[1::2])  # noei

# convert uppercase / lowercase
print(x.upper())    # INDONESIA: uppercase
print(x.lower())    # indonesia: lowercase
