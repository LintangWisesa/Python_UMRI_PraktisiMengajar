# Functional Programming
# the 4th concept: functions are first class & can be higher order

# higher order func:
# 1. func as an arg of another func
def pi():
    return 3.14
def luasLingkaran(pi, radius):
    # luas lingkaran = pi.r.r
    return pi * (radius ** 2)
print(luasLingkaran(pi(), 7)) # lingkaran dg r = 7cm
print(luasLingkaran(pi(), 14)) # lingkaran dg r = 14cm

# 2. func as return value of another func
def hitungPi():
    return pi()
print(hitungPi())