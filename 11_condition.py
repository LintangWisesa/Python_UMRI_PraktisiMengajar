a = 5
b = 5
c = "5"
print(a == b)   # True
print(a == c)   # False
print(a != c)   # True
print(a > b)    # False
print(a < b)    # False
print(a >= b)   # True
print(a <= b)   # True

print(10 > 9)   # True
print(8 < 7)    # False

# x AND y = TRUE jika x = TRUE & y = TRUE
print((10>9) and (8<7)) # True and False = FALSE
print(True and True)
print((10>9) and (9>1))

# x OR y = TRUE jika salah satu x / y = TRUE
print(True or True)
print((10 < 12) or (100 > 1))
print((10 < 2) or (100 > 1))
print((10 < 2) or (100 < 1))

# NOT = membalik kondisi TRUE => FALSE dan sebaliknya
print(not True)
print(not False)
print(100 > 90)
print(not 100>90)

x = {"name": "Agus"}
print(x["name"] == "Budi")