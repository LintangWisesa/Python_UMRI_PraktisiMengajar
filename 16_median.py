# MEDIAN: nilai tengah dari list yang disortir
x = [1, 2, 4, 5, 12, 1, 99, 6, 5, 8, 45, 120]

x.sort()
print(x)

iMedian = 0
median = 0
if len(x) % 2 == 0:     # dibagi 2 sisanya = 0 maka len(x) = genap
    iMedian = [int((len(x) / 2) - 1), int(len(x) / 2)]
    median = (x[iMedian[0]] + x[iMedian[1]]) / 2
else:
    iMedian = [int(len(x) / 2)]
    median = x[iMedian[0]]
print(median)


# 1, 2, 3, 4, 5       len(x)=5 median=index 2  ganjil 5/2 = 2.5 = 2
# 1, 2, 3, 4, 5, 6    len(x)=6 median=i 2&3    genap  6/2 = 3   = 3-1, 3


