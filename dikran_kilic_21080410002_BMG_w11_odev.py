# “kisiler” isimli bir liste olusturunuz.
kisiler = ["dikran", "meryem" ,"ali", "zeyneb"]
list=[]
print(kisiler)

#Ekrandan isim giriniz
list = input("isimleri giriniz=")
kisiler.append(list)

#Listeyi ekrana yazdiriniz
print(kisiler)

#Listenin uzunlugunu  yazdiriniz.
print(len(kisiler))

#Listenin 2. elemanini ekrana yazdiriniz
print(kisiler[1])

#Listenin son elemanini listeden siliniz. 
kisiler.pop(4)

#Listeyi tekrar yazdiriniz.
kisiler.append(list)
print(kisiler)