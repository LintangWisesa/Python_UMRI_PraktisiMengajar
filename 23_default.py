# Default Arg Value

def halo(nama):
    print(f"Halo {nama}")

halo("Andi")
halo("Budi")
# halo()          # halo() missing 1 required positional argument: 'nama'

def aloha(nama="Lintang"):
    print(f"Aloha {nama}")
aloha("Budi")
aloha()