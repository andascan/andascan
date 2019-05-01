# -*- coding: utf-8 -*-
"""
Created on Wed May  1 14:19:05 2019

@author: andaşcan
"""

import numpy as np
import matplotlib.pyplot as plt
import os

path1 = os.getcwd()                 #hangi klasörde çalışılıyorsa onun path'ini buluyor
path2 = path1 + '\\100_Airfoil'     #path2 airfoil dosyalarını içeren klasörü açar.
path4 = path1 + '\\Normalized_Airfoil_Data_Set'          # Airfoil data klasörü oluşturur.
if not os.path.exists(path4):       #Eğer klasör yoksa klasörü oluşturur.
    os.makedirs(path4)

List_a = os.listdir(path2)          #List_a 100 tane airfoil listesini oluşturur. 

for i in range(len(List_a)):        #liste uzunluğu kadar for döngüsü oluşturuldu.
   
    path3 = path2 + '\\' + List_a[i]        #path 3 tek tek airfoil datalarının alınması için oluşturuldu.
    with open(path3, 'r') as file:          # Geometry loaded from data file
            header = file.readline()           # Her bir airfoil'in başlığının gözükmesi için komut yazıldı.
            x, y = np.loadtxt(file, dtype=float, unpack=True)  
    
    x_l, y_l = x.tolist(), y.tolist()  # tolist() is used to convert a series to list.

    x_last = x_l[-1]
    y_last = y_l[-1]                              
    x_l.insert(0, x_last) 
    y_l.insert(0, y_last)                       
    
    x_v , y_v = x.reshape(len(x),1), y.reshape(len(y),1)
    xy   = np.hstack((x_v, y_v))    #iki tane array'i yanyana birleştiriyor.
    
    plt.figure(figsize=(12,12))        
    plt.plot(x,y, '-')
    plt.title(header, loc='center')                 #başlık ve yer kodları
    plt.axes().set_aspect('equal')                  #aspect ratiosunu 1 olarak ayarlıyor.
    plt.xlim(min(x) - 0.02,max(x) + 0.02)          
    plt.ylim(min(y) - 0.02, max(y) + 0.025)
    plt.show()
    plt.savefig(path4 + '\\' + List_a[i] + '.jpeg', dpi = 300) 
    np.savetxt( path4 + '\\' + List_a[i] + '.txt', xy)
        