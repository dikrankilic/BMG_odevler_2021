#sinav_sonuc isimli sözlük olusturulur
sinav_sonuc = {'isimler':['ayse k.','ahmet m.','nuri c.','nawwar t.','suzan t.','ala b.'],
'cinsiyet':['k','e','e','e','k','k'],
'matematik':[60,40,97,45,56,95],
'türkce':[70,30,23,80,78,46]
}
#Kullinicinin klavyeden girdiği bilgileri sinav_sonuc isimli sozluge eklenir
def ogrenci_bilgileri_guncelleme(isim,cinsiyeti,matematiknot,türkçe):
   sinav_sonuc['isimler'].append(isim)
   sinav_sonuc['cinsiyet'].append(cinsiyeti)
   sinav_sonuc['matematik'].append(matematiknot)
   sinav_sonuc['türkce'].append(türkçe)
   


#Kullanicidan  klavyeden 2 yeni bilgi girmesi istenir
isim_1=input('1.Öğrencinin ismini"isim soyismin_ilk_harfi." olarak giriniz:')
cinsiyet_1=input("Öğrencinin cinsiyeti erkek ise e Kız ise k harfini giriniz.")
matematik_1=input("Öğrencinin matematik dersinden aldığı notu giriniz:")
Türkçe_1=input("Öğrencinin Türkçe dersinden aldığı notu giriniz:")

ogrenci_bilgileri_guncelleme(isim_1,cinsiyet_1,matematik_1,Türkçe_1)


isim_2=input('2. Öğrencinin ismini"isim soyismin_ilk_harfi." olarak giriniz:')
cinsiyet_2=input("Öğrencinin cinsiyeti erkek ise e Kız ise k harfini giriniz.")
matematik_2=input("Öğrencinin matematik dersinden aldığı notu giriniz:")
Türkçe_2=input("Öğrencinin Türkçe dersinden aldığı notu giriniz:")

ogrenci_bilgileri_guncelleme(isim_2,cinsiyet_2,matematik_2,Türkçe_2)


#Girilen yeni bilgi ile birlikte güncellenmis olan tabloyu ekrana yazdirilir
print(sinav_sonuc)
print("İsimler:",sinav_sonuc['isimler'])
print("Cinsiyetleri (e olanlar erkek, kız olanlar k harfiyle gösterilmiştir.):",sinav_sonuc['cinsiyet'])
print("Matematik derslerinden alınan notlar:",sinav_sonuc['matematik'])
print("Türkçe dersinden alınan notlar:",sinav_sonuc['türkce'])
print("Not:cinsiyet ve notlar, isim listesine göre sırasıyla yazılmıştır.")