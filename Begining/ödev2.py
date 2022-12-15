#Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
#Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
print("merhabalar!! Beden kitle indeksi hesaplamaya hoş geldiniz...")
boy = float(input("Lütfen Boyunuzu giriniz ="))
kilo = int(input("Lütfen Kilonuzu giriniz ="))
indeks = kilo / (boy ** 2)

print("beden kitle indeksiniz = {}".format(indeks))

