# Arbitrary Keyword Arguments
# belum tahu pasti ada brp keyword arg yg seharusnya ada dalam function

def halo(**kwargs):
    # **kwargs bisa diakses dalam func sbg dictionary
    # print(kwargs)
    print(f"Halo {kwargs['nama']}")
halo(nama="Lintang", usia=25, job="Backend Developer")
halo(alamat="Jl. XYZ 13 Jakarta", telephone="0271-123321", nama="Budi")

def statistics(**kwargs):
    print(kwargs["mean"])
    print(kwargs["median"])
    print(kwargs["modus"])
statistics(mean=12, median=34, modus=5)
statistics(median=34, mean=20, modus=5)