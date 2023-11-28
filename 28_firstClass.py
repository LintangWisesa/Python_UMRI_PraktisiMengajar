# Functional Programming
# the 4th concept: functions are first class & can be higher order
# dalam pemrograman 1st class component = VARIABLE

# what are 1st class citizens?
# 1. assign / store data
x = 20
y = "Andi"
z = True

# 2. pass as func args
y = "Bambang"
def hello(nama):
    print(f"Hello {nama}!")
hello(y)

# 3. return func
def hi():
    z = "Caca"
    return z
print(hi())
print(hi())

# 4. store in a data structures: list, set, tuple, dictionary
x = "Andi"
students = ["Ali", "Kiki", "Belinda", x]
print(students)