#Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
#Hipotenüs Formülü: a^2 + b^2 = c^2
x = int(input("1.dik kenarı giriniz= "))
y = int(input("2.dik kenarı giriniz= "))

hipotenüs =(x ** 2 + y ** 2) ** 0.5
print("hipotenüs değeri= {}".format(hipotenüs))