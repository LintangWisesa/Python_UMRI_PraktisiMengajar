# Functional Programming
# the 4th concept: functions are first class & can be higher order
# dalam pemrograman 1st class component = VARIABLE

# what are 1st class citizens?
# 1. assign / store data => return function
def hello():
    return "Hello"
print(hello())

# 2. pass as func args
def sayWorld(x):
    return x + " World!"
print(sayWorld(hello()))

# 3. return func
def sayHello():
    return hello()
print(sayHello())

# 4. store in a data structures: list, set, tuple, dictionary
students = ["Andi", "Belinda", "Caca", hello()]
students2 = ("Andi", "Belinda", "Caca", hello())
students3 = {"Andi", "Belinda", "Caca", hello()}
students4 = {
    "nama": hello()
}
print(students)
print(students2)
print(students3)
print(students4)