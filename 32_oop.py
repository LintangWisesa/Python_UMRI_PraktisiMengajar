# OOP: object & class
# object = hasil cetakan dari class
# class = template / blueprint / cetakan

# class dengan 1 property data: x=5 & 1 property func: y()
class ContohClass:
    x = 5                           # property - data
    def kaliSeratus(self):          # property - func (method)
        return self.x * 100

# object z from class ContohClass
z = ContohClass()
print(z)
print(z.x)
print(z.kaliSeratus())

# cetakan jelly
class CetakanJelly():
    warna = 'cokelat'
    rasa = 'cokelat'
    def addTopping(self):
        return 'Jelly Cokelat Meses'

# create object
a = CetakanJelly()
print(a.warna, a.rasa, a.addTopping())
b = CetakanJelly()
print(b.warna, b.rasa, b.addTopping())