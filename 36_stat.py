
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# class Stat
class Stat():
    def __init__(self, listAngka):
        self.listAngka = listAngka
    def mean(self):
        return sum(self.listAngka) / len(self.listAngka)

myStat = Stat(x)
print(myStat.mean())