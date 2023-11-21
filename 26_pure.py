# Concepts of Functional Programming
# 1. Pure functions
# 2. Recursion
# 3. Referential transparency
# 4. Functions are First-Class and can be Higher-Order

# Pure Function:
# 1. Functions selalu memiliki output yg sama untuk arg input yg sama
def pangkatDua(x):
    return x ** 2
print(pangkatDua(5))       # output harus = 25
print(pangkatDua(5))       # output tetap 25

# 2. Functions tidak berefek/memodifikasi global variable & arg input
a = 12
def tes(x, y):
    x = 10      # forbidden in func programming
    y = 12      # forbidden
    a = 8       # forbidden
    print(x, y, a)
tes(99, 98)
print(a)
