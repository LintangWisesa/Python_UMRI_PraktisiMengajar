
def hello():
    print("Hello World!")
hello()
hello()
print(hello())

def hi():
    print("Hi!")
hi()

# argument: value yang disisipkan ke dalam function
def aloha(nama):
    print(f"Aloha {nama}!")
aloha("Lintang")
aloha("Andi")

def halo(nama, usia, kota):
    print(f"Halo {nama}, usiamu {usia} asal dari kota {kota}")
halo("Budi", 25, "Jakarta")
halo(23, "Bandung", "Andi")

# function untuk menghitung mean
def mean(listAngka):
    mean = int(sum(listAngka) / len(listAngka))
    print(f"Mean dari {listAngka} = {mean}")
x = [1, 2, 3, 4, 5]
mean(x)