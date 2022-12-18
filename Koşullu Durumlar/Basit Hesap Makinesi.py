print("""*********************
HESAP MAKİNASI PROGRAMI :)
İŞLEMLER:
1)toplama
2)çıkarma
3)çarpma
4)bölme
**************************""")
a = int(input("birinci sayıyı giriniz: "))
b = int(input("ikinci sayıyı giriniz: "))

işlem = input("işlem giriniz:")
if işlem == "1":
    print("{} in {} ile toplamı {}'dir.".format(a,b,a+b))
elif işlem == "2":
    print("{} in {} ile farkı {} dır.".format(a,b,a-b))
elif işlem =="3":
    print("{} in {} ile çarpımı {} dir.".format(a,b,a*b))
elif işlem == "4":
    print("{} in {} ile bölümü {} dir.".format(a,b,a/b))
else:
    print("Geçersiz İşlem............")
