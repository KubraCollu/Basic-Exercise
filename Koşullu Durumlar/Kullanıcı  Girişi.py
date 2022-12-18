print("""*********************
Kullanıcı Girişi Programı
********************""")

sys_kullanıcı_adı = "kübra"
sys_parola = "22061998"

kullanıcı_adı = input("Kullanıcı Adı Giriniz: ")
kullanıcı_parola = input("Kullanıcı Parolayı Giriniz: ")

if (kullanıcı_adı == sys_kullanıcı_adı and kullanıcı_parola != sys_parola):
    print("parola yanlış girilmiştir!")
elif (kullanıcı_adı != sys_kullanıcı_adı and kullanıcı_parola == sys_parola):
    print("Kullanıcı adı yanlış girilmiştir!")
elif (kullanıcı_adı != sys_kullanıcı_adı and kullanıcı_parola != sys_parola):
    print("Kullanıcı adı ve parola yanlış girilmiştir!!!")
else:
    print("Sisteme Başaryla Giriş Yaptınız......")

