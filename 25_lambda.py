
def x(a):
    return a
y = x(10)

print(x(10))
print(y)

# Lambda: small anonymous func
y = lambda a : a    # y adalah lambda func dg arg a yang mereturn a
print(y(10))

def y(a):
    return a

kali = lambda x, y: x * y
print(kali(2, 2))
print(kali(3, 10))

bagi = lambda x, y: x / y
print(bagi(6, 2))
print(bagi(10, 5))