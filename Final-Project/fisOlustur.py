########################################################################################################################
#                                        Veri Madenciliği Dönem Sonu Projesi                                           #
#                                              Mehmet Emin KONUK                                                       #
#                                                  22283549                                                            #
########################################################################################################################
urunler = [("Tam yağlı süt (1 litre)",10),
("Yumurta (30 adet)",10),
("Ekmek (250 gram)",10),
("Beyaz peynir (500 gram)",10),
("Yoğurt (3 kg)",1),
("Domates (1 kg)",1),
("Patates (3 kg)",1),
("Soğan (3 kg)",1),
("Makarna (500 gram)",1),
("Pirinç (1 kg)",1),
("Toz Şeker (3kg)",10),
("Çay (3 kg)",1),
("Su (5 litre)",10),
("Ayçiçek yağı (5 litre)",10),
("Un (1 kg)",10)]

import random
from openpyxl import Workbook

def fiş_oluştur(urunler, fiş_sayısı, min_ürün_sayısı, max_ürün_sayısı):
    fişler = []
    fiş_kodu = 9894 

    for _ in range(fiş_sayısı):
        fiş = {
            "fiş_kodu": str(fiş_kodu).zfill(12),
            "ürünler": []
        }

        ürün_sayısı = random.randint(min_ürün_sayısı, max_ürün_sayısı)

        for _ in range(ürün_sayısı):
            ürün = random.choices(urunler, weights=[sıklık for _, sıklık in urunler])[0]
            fiş["ürünler"].append(ürün)

        fişler.append(fiş)
        fiş_kodu += 1

    return fişler

fişler = fiş_oluştur(urunler, 200, 10, 10)

wb = Workbook()
sheet = wb.active

sheet["A1"] = "FISNO"
sheet["B1"] = "URUN"

row_index = 2
for fiş in fişler:
    fiş_kodu = fiş["fiş_kodu"]
    for ürün in fiş["ürünler"]:
        sheet[f"A{row_index}"] = fiş_kodu
        sheet[f"B{row_index}"] = f"{ürün[0]}"
        row_index += 1

# Excel dosyasını kaydet
wb.save("fişlerYeni.xlsx")




##############################################################################################################################################################################################
# urunler = [("Tam yağlı süt (1 litre)",10),
# ("Yumurta (30 adet)",10),
# ("Ekmek (250 gram)",10),
# ("Beyaz peynir (500 gram)",10),
# ("Yoğurt (3 kg)",10),
# ("Salatalık (500 gram)",8),
# ("Domates (1 kg)",10),
# ("Patates (3 kg)",10),
# ("Soğan (3 kg)",10),
# ("Havuç (1 kg)",4),
# ("Mısır gevreği (2 kg)",2),
# ("Makarna (500 gram)",10),
# ("Pirinç (1 kg)",10),
# ("Bulgur (1 kg)",10),
# ("Dana biftek (500 gram)",6),
# ("Tavuk göğsü (1 kg)",8),
# ("İrmik (500 gram)",5),
# ("Toz Şeker (3kg)",10),
# ("Tam buğday unu (1 kg)",10),
# ("Küp şeker (1 kg)",10),
# ("İyotlu tuz (500 gram)",10),
# ("Zeytinyağı (2 litre)",6),
# ("Ayçiçek yağı (5 litre)",10),
# ("Bezelye (500 gram)",3),
# ("Kuru fasulye (1 kg)",8),
# ("Yeşil mercimek (500 gram)",8),
# ("Nohut (1 kg)",9),
# ("Mantar (250 gram)",5),
# ("Ceviz (200 gram)",2),
# ("Badem (200 gram)",1),
# ("Kabuklu fındık (200 gram)",2),
# ("Ayva (1 kg)",1),
# ("Portakal (1 kg)",7),
# ("Elma (1 kg)",7),
# ("Armut (1 kg)",4),
# ("Şeftali (1 kg)",4),
# ("Muz (1 kg)",4),
# ("Çilek (250 gram)",2),
# ("Kırmızı üzüm (500 gram)",1),
# ("Kivi (500 gram)",1),
# ("Ananas (1 adet)",1),
# ("Limon (1 kg)",8),
# ("Nar (500 gram)",2),
# ("Sıvı Sabun (1 litre)",9),
# ("Tereyağ (1kg)",10),
# ("Su (5 litre)",10),
# ("Şeftalili soğuk çay (1 litre)",7),
# ("Maden suyu (6 adet)",7),
# ("Limonata (2 litre)",4),
# ("Ayran (1 litre)",7),
# ("Çamaşır Yumuşatıcısı (2 litre)",8),
# ("Çamaşır Suyu (1 litre)",10),
# ("Gazoz  (1 litre)",4),
# ("Tuvalet Kağıdı (32 adet)",10),
# ("Kaşar Peynir (250 gram)",6),
# ("Çubuk Kraker (1 adet)",8),
# ("Bütün Tavuk (1 adet)",10),
# ("Çöp Poşeti (1 adet)",10),
# ("Çekirdek (1 kg)",8),
# ("Patates cipsi (200 gram)",8),
# ("Mantı (250 gram)",3),
# ("Dondurulmuş Pizza (1 adet)",3),
# ("Dondurulmuş Burger köfte (4 adet)",2),
# ("Sucuk (200 gram)",9),
# ("Külah Dondurma (1 adet)",5),
# ("Türk kahvesi (250 gram)",8),
# ("Yeşil çay (100 adet poşet)",1),
# ("Bal (500 gram)",6),
# ("Çikolata (100 gram)",9),
# ("Kola (2 litre)",9),
# ("Fanta (2 Litre)",4),
# ("Piliç Salam (500 gr)",5),
# ("Limonata (1 litre)",3),
# ("Sivri Biber (500 gr)",9),
# ("Enerji içeceği (250 ml)",3),
# ("Meyve Suyu (1 litre)",3),
# ("Çay (3 kg)",10),
# ("Zeytin (500 gram)",10),
# ("Su (250ml)",10),
# ("Tavuk göğsü (500 gram)",7),
# ("Köfte harcı (500 gram)",1),
# ("Dondurma (1 litre)",1),
# ("Susamlı Kraker (200 gram)",5),
# ("Ton Balığı (500 gram)",5),
# ("Çikolatalı gofret (50 gram)",5),
# ("Karpuz (8 kg)",4),
# ("Mayonez (400 gram)",7),
# ("Ketçap (500 gram)",7),
# ("Peçete (200 adet)",10),
# ("Şampuan (300 gram)",10),
# ("Deodorant (200cl)",6),
# ("Parfüm (100cl)",6),
# ("Diş Macunu (75 ml)",10),
# ("Fındık ezmesi (350 gram)",4),
# ("Bulaşık Deterjanı (3 litre)",9),
# ("Paketli Kek (500 gram)",3),
# ("Patlıcan (500 gram)",7),
# ("Sandviç ekmeği (400 gram)",4),
# ("Karabiber (100 gram)",8),
# ("Marul (1 adet)",9)]