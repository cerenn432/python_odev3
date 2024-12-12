sayilar = [3,5,7,2,12,32,45]
# 1- "sayilar" listesindeki her bir elemanı yazdırınız.

print(*sayilar)

# 2- "sayilar" listesinde hangi sayılar 3' ün katıdır?

for sayi in sayilar:
   if (sayi%3==0):
       print(sayi)

# 3- "sayilar" listesinde tüm sayıların toplamı nedir?

toplam = 0
for sayi in sayilar:
    toplam += sayi
print('toplam:',toplam)


urunler = ["iphone 13","samsung s24","samsung s22","iphone 15","iphone 14"]

# 4- "urunler" listesindeki tüm iphone marka ürünleri listeleyiniz. (index ve find komutlarından faydalanınız.)
iphonelar=[]
for urun in urunler:
    if urun.find("iphone") !=-1:
        iphonelar.append(urun)

print("Iphone ürünleri: " , iphonelar)


# 5- "urunler" listesinde kaç adet samsung ürünü vardır? (find metodu)

samsunglar=[]
for urun in urunler:
    if urun.find("samsung") !=-1:
        samsunglar.append(urun)

print("Samsungların sayısı: " +str(len(samsunglar)))