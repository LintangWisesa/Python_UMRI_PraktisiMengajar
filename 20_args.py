# Arbitrary Arguments
# Belum tahu pasti, sebuah func seharusnya punya berapa arguments

def test(*args):
    # *args bisa diakses sebagai tuple
    print(args)
    print(args[0], args[1], args[2])

test("Args 1", "Args 2", "Args 3")
test("Args 1", "Args 2", "Args 3", "Args 4", "Args 5")

def fullName(*nama):
    namaLengkap = ""
    for i in nama:
        namaLengkap = namaLengkap + i + " "
    print(namaLengkap)
fullName("Andi", "Susilo")
fullName("Budi", "Nur", "Wicaksono")
fullName("Soleh")
fullName("Edi", "Nur", "Fajri", "Yanto")