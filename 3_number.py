# Number: numeric data value
x = 12      # int: bilangan bulat
y = 3.14    # float: desimal
z = 4j      # complex: j = akar pangkat dua dari -1 (imajiner)
a = 1e3     # float: e = 10 pangkat x, 1e3 = 1 x 10 pangkat 3
b = 1e-10   # float: e = 10 pangkat x, 1e3 = 1 x 10 pangkat -10

# type(): check data type
print(type(x))
print(type(y))
print(type(z))
print(f"Hi I'm {x} yo, weight {y} and height {z}")
print(a)
print(type(a))
print(b)

# mathematic operator
print(x + 2)    # penjumlahan
print(x - 2)    # pengurangan
print(x * 2)    # perkalian
print(x / 2)    # pembagian. int / int = result float
print(x ** 2)   # pangkat
print(x % 2)    # modulus / sisa bagi