# DICTIONARY: python collection, key:value, indexed, mutable, tdk boleh ada duplikat

x = {
    "name": "Andi",
    "age": 20,
    "job": "Mahasiswa",
    "isMarried": False,
}
y = {
    1: "Senin",
    2: "Selasa",
    3: "Rabu",
    4: "Kamis",
    5: "Jumát",
    6: "Sabtu",
    7: "Ahad"
}

print(x)
print(x["name"])
print(x.get('name'))

print(type(y))
print(y[3])

# mendaftar keys pada dict
print(x.keys())     # mendaftar keys pada dict x
print(list(x))      # dict => list = list of keys

x['name'] = 'Budi'
print(x)
x['address'] = "Jl. XYZ No. 34 Riau"
print(x)
x.pop('job')
print(x)