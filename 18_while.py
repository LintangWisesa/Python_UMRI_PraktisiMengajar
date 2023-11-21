
x = [10, 20, 30, 40, 50]

for i in x:
    print(i)

i = 0
while i < len(x):
    print(x[i])
    i += 1

# jika elemen = 30, tolong dibreak
i = 0
while i < len(x):
    print(x[i])
    if x[i] == 30:
        break
    i += 1

# jika elemen = 30, tolong diskip
i = 0
while i < len(x):
    if x[i] == 30:
        continue
    print(x[i])
    i += 1
    