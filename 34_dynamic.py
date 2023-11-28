
# cetakan jelly
class CetakanJelly():
    def __init__(self, warna, rasa, topping):
        self.warna = warna
        self.rasa = rasa
        self.topping = topping
    def addTopping(self):
        return self.topping

# create object
a = CetakanJelly("orange", 'jeruk', 'oreo')
print(a.warna, a.rasa, a.addTopping())
b = CetakanJelly('merah', 'buah naga', 'meses')
print(b.warna, b.rasa, b.addTopping())
c = CetakanJelly('hijau', 'jambu', 'selai strawberry')
print(c.warna, c.rasa, c.addTopping())