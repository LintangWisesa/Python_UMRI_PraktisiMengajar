# IF statement
# ujian akan dianggap lulus jika nilai >= 70
nilai = 85
if nilai >= 70:
    print("Anda lulus")
else:
    print("Tidak lulus")

# IF ELIF ELSE statement
# ujian lulus jika nilai >= 70, tidak lulus jika < 50 & bisa remidi jika 50-69
nilai = 50
if nilai >= 70:
    print("Anda lulus")
elif nilai < 50: 
    print("Anda tidak lulus")
else:
    print("Anda berhak remedial") 

# one line if statement
# y = True jika x > 20 selain itu y = False
x = 21
if x > 20:
    y = True
else:
    y = False
print(y) 

x = 1
y = True if x > 20 else False
print(y)