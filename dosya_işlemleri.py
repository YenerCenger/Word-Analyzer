class Dosya():

    def __init__(self):

        with open("metin.txt","r",encoding= "utf-8") as file:

            dosya_içeriği = file.read()

            kelimeler = dosya_içeriği.split()

            self.sade_kelimeler = []



            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")

                i = i.lower()
                self.sade_kelimeler.append(i)

    def tüm_kelimeler(self):

        kelimeler_kümesi = set()

        for i in self.sade_kelimeler:
            kelimeler_kümesi.add(i)

        print("Tüm Kelimeler......")

        for i in kelimeler_kümesi:
            print(i)
            print("********")

    def kelime_frekansı(self):

        kelime_sözlük = dict()

        for i in self.sade_kelimeler:

            if i in kelime_sözlük:
                kelime_sözlük[i] += 1

            else:
                kelime_sözlük[i] = 1

        for kelime,sayı in kelime_sözlük.items():

            print("{} kelimesi {} defa geçiyor....".format(kelime,sayı))

            print("------------------------")

    def kelime_bul(self,kelime):
        self.kelime = kelime
        kelime_sayaç = 0
        for i in self.sade_kelimeler:
            if i == kelime:
                kelime_sayaç += 1

        if kelime_sayaç == 0:
            print("{} kelimesi metinde geçmiyor.".format(kelime))

        else:
            print("{} kelimesi metinde {} kez geçiyor.".format(kelime,kelime_sayaç))



dosya = Dosya()
dosya.tüm_kelimeler()

dosya.kelime_bul("yakın")