class PersegiPanjang:
    panjang = 0
    lebar = 0

    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    def luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return "persegi panjang, panjang " + str(self.panjang) + " cm, dan lebar " + str(self.lebar) + " cm"
    
