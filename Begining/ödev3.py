#Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.
print("Merhabalar:) arac benzin istasyonuna hoş geldiniz. \nLütfen borcunuzu öğrenmek için istenilen bilgileri girininiz...")
x = float(input("Aracınızın KM Başı  Yakıt Masrafı = $ "))
y = float(input("Alınan yol (km) = km "))
toplam = x * y
print("sürücünün toplam yakıt borcu = {}$\nBizi tercih ettiğiniz için teşekkürler dileriz..\nİYİ YOLCULUKLAR...".format(toplam))