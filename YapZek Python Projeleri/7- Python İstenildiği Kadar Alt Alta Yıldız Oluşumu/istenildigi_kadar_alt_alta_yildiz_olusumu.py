# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 20:11:53 2021

@author: Monster
"""

"""

proje adı : istenildiği kadar alt alta yıldız oluşumu.

*
**
***
****
*****

"""





"""
Hilmi Tarık BALCI Tarafından Kodlanmıştır.

9.11.2021
"""

yildiz = int(input("yildiz satır sayısını giriniz -> "))
for yildiz_sonuc in range(1,yildiz+1,1):
  print(yildiz_sonuc*"*")