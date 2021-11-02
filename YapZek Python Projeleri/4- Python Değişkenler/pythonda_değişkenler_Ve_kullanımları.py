# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 20:18:20 2021

@author: Monster
"""

# Değişkenlerin anlatımı ve değişken tiplerini öğrenmek

urun = "etek"
urun_fiyati = 50
urun_ebatı = 3.8

print(type(urun))
print(type(urun_fiyati))
print(type(urun_ebatı))

# değişkenleri biribirine eşitleyerek hepsinin değerinin
# aynı olması sağlandı.
urun1 = urun2 = urun3 = "portakal"
# print ifadesini kullanarak test ediniz.

# python değişken oluşturma farklı yöntem:
urun1, urun_fiyati1, urun_ebati = "kazak", 39.90, "XXL"
# print ifadesi kullanarak çıktı yaptırınız.

kulup_adi = "yapzek"
kulup_kurulus_tarihi = 2021

print(kulup_adi + " tarihinde " + str(kulup_kurulus_tarihi) + " kurulmuştur.")