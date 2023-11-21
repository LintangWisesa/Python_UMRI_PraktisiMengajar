# Keyword Arguments
# memanggil func berargumen berdasarkan keyword argumentnya

def halo(nama, usia, job):
    print(f"Halo {nama}, usiamu {usia} dan bekerja sebagai {job}")
halo("Andi", 22, "Backend Developer")
halo(21, "Data Scientist", "Budi")

# dengan kwargs, kita bisa call func berargumen tanpa perlu perhatikan urutan
# tapi perlu perhatikan nama argumen
halo(nama="Ali", usia=25, job="Frontend Developer")
halo(usia=25, nama="Banu", job="Database Admin")