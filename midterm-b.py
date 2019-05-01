# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 13:42:13 2019

@author: andaşcan
"""

import numpy as np
import matplotlib.pyplot as plt
import os

path1 = os.getcwd()                 #hangi klasörde çalışılıyorsa onun path'ini buluyor
path2 = path1 + '\\100_Airfoil'     #path2 airfoil dosyalarını içeren klasörü açar.
path_image = path1 + '\\Images'

List_a = os.listdir(path2)          #List_a 100 tane airfoil listesini oluşturur. 
bad_airfoils = []                   #bad airfoils boş listesi oluşturuldu çünkü çizilemeyen veya hata olan airfoiller burada gözükecek.

def airfoil_data(x,y):
     
    x_l, y_l = x.tolist(), y.tolist()  # tolist() is used to convert a series to list.
    # chordline
    ind_min = x_l.index(min(x_l))      #x listesindeki minimum index belirlendi. 
    x_ch = [min(x_l), max(x_l)]        #chordline çizdirmek için min ve max x,y noktaları belirlendi.
    y_ch = [y_l[ind_min], y_l[ind_min]]        
    # mean camberline
    x_mc, y_mc = [], []  #mean camber line için boş listeler oluşturuldu.
    x_mc.append(x_ch[0]), y_mc.append(y_ch[0]) #Airfoilin Leading edge'i mcl'ın ilk noktaları olarak x ve y cinsinden listeye atıldı.
    
    t_x, t_y, thickness, max_thickness = [], [], 0, 0 # thickness bulmak için t_x ve t_y listeleri oluşturuldu.
    x_up, x_down = x_l[:ind_min], x_l[ind_min+1:]    # x önce artıp sonra azaldığı için, yukardaki kısımlar x_up, alttaki kısımlar x_down oldu.
    y_up, y_down = y_l[:ind_min], y_l[ind_min+1:]    # Ve bunlar x_list'in içindeki minimum değerin index'ini verir.
    x_up.reverse(), y_up.reverse()                   #x_up ve y_up değerlerinin bulunduğu liste tersine çevrilir çünkü ikisinin de leading *
                                                     #edge'den başlamasını istiyoruz.
    for i in range(min(len(y_up),len(y_down))):      # y_up ve y_down listelerindeki eleman sayısının minimum olanına göre işlem yapıyor. 
        x_mc.append(0.5*(x_up[i]+x_down[i]))         #Up ve down'daki değerleri toplayıp ortalamasını alıyor. Bu da bize mean camber line *
                                                     #noktalarını veriyor. 
        y_mc.append(0.5*(y_up[i]+y_down[i]))
        
        thickness = y_up[i] - y_down[i]             #Bu y değerlerinin farkı bize thickness değerini veriyor.
        if thickness > max_thickness:               #max thickness'ı bulmak için bu döngü oluşturuluyor.
            max_thickness = thickness
            t_x = [x_up[i], x_down[i]]              #Thickness'ların x ve y noktasılarını veriyor.
            t_y = [y_up[i], y_down[i]]
    
    x_mc.append(x_ch[1]), y_mc.append(y_ch[1])       #Burda da en son trailing edge'ler eklendi.
    
    plt.figure(figsize = (12,12))
    plt.plot(x,y, '-')                             #airfoil çizdiren kod.
    plt.plot(x_ch, y_ch, 'r-')                      #chord line çizdiren kod
    plt.plot(x_mc, y_mc, 'g-.')                     #mean chamber line çizdiren kod.
    plt.plot(t_x, t_y, 'k-')                        #thickness gösterimi.
    plt.title(header, loc='center')                 #başlık ve yer kodları
    plt.xlim(min(x) - 0.02,max(x) + 0.02)          
    plt.ylim(min(y) - 0.02, max(y) + 0.025)
    plt.axes().set_aspect('equal')                  #aspect ratiosunu 1 olarak ayarlıyor.
#    plt.savefig(path_image + '\\' + List_a[i] + '.jpeg')   
    plt.show() 
    
    return 

for i in range(len(List_a)):        #liste uzunluğu kadar for döngüsü oluşturuldu.
    
    try:                                        #açılamayan veya hata olan airfoil dosyalarını listeye kaydetmek için 
                                                #try and except komutu oluşturuldu
        path3 = path2 + '\\' + List_a[i]        #path 3 tek tek airfoil datalarının alınması için oluşturuldu.
        with open(path3, 'r') as file:          # Geometry loaded from data file
            header = file.readline()           # Her bir airfoil'in başlığının gözükmesi için komut yazıldı.
            x, y = np.loadtxt(file, dtype=float, unpack=True)   #Metin dosyasının içinde bulunan x ve y noktalarına göre airfoiller çizildi.
        airfoil_data(x,y)

    except:
        bad_airfoils.append(List_a[i])

print(bad_airfoils)
    
