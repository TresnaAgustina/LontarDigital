class Tokenisasi:
    def __init__(self):
        self.inputan = ""
        self.hasil = ""
        self.hasil_pecah = ""
        self.jumlah = 0
        self.hasillooping = []

    def etokenisasi(self, teks):
        # Penggantian karakter
        self.inputan = teks
        percobaan = self.inputan.replace(" ", "%")
        percobaan = percobaan.replace("\n", "%")
        percobaan = percobaan.replace(".", " x ")
        percobaan = percobaan.replace(",", " z ")
        percobaan = percobaan.replace(" ", "%")

        # Pemisahan dengan Split
        wordz = percobaan.split('%')
        self.jumlah = len(wordz)

        # Penggantian lainnya
        for loop in range(self.jumlah):
            wordz[loop] = wordz[loop].replace('x', '.')
            wordz[loop] = wordz[loop].replace('z', ',')

        # Pengolahan token
        hasilkata = []
        self.hasillooping = hasilkata
        for x in range(self.jumlah):
            hasilkata.append(wordz[x])
            self.hasil_pecah = hasilkata[x]

        # Gabungan string setelah di split %
        y = ''.join(wordz)
        self.hasil = y

        return percobaan
