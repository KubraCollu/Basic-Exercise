#Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.
isim =input("isminizi giriniz = ")
soyisim =input("soy isminizi giriniz = ")
numara =int(input("numaranızı giriniz = "))
bilgiler = [isim, soyisim, numara]
print("kişinin isim = {} \nkişinin soyisim = {} \nkişinin numara = {} ".format(bilgiler[0],bilgiler[1],bilgiler[2]))
