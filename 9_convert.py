# KONVERSI list <=> tuple <=> set

x = [1, 2, 3, 4, 5]
print(x)
print(type(x))

y = tuple(x)
print(y)
print(type(y))

z = set(y)
print(z)
print(type(z))

a = list(z)
print(a)
print(type(a))

# list = allow duplicate | set = tidak boleh duplicate
# apa yg terjadi jika list dg duplicate => konversi ke set?
b = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]
c = set(b)
print(b)
print(c)