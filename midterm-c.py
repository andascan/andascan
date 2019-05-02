# -*- coding: utf-8 -*-
"""
Created on Wed May  1 16:24:53 2019

@author: andascan
"""

import numpy as np
import matplotlib.pyplot as plt
import os

path1 = os.getcwd()                 #hangi klasörde çalışılıyorsa onun path'ini buluyor
path2 = path1 + '\\100_Airfoil'     #path2 airfoil dosyalarını içeren klasörü açar.

List_a = os.listdir(path2)

for i in range(len(List_a)):        #liste uzunluğu kadar for döngüsü oluşturuldu.
   
    path3 = path2 + '\\' + List_a[i]        #path 3 tek tek airfoil datalarının alınması için oluşturuldu.
    with open(path3, 'r') as file:          # Geometry loaded from data file
            header = file.readline()           # Her bir airfoil'in başlığının gözükmesi için komut yazıldı.
            x, y = np.loadtxt(file, dtype=float, unpack=True)  
    
    x, y = x.tolist(), y.tolist()

def panels(x,y,N=20):
    
    radius =   (max(x)) - (min(x)) / 2 #dairenin yarıçapını verir  
    merkez_x = (max(x)) - (min(x)) / 2 #dairenin merkezinin x koordinatı
    
    theta = np.linspace(0.0, 2* np.pi, N + 1) #2pi 21 parçaya bölündü, 1 derece artıyor.
    daire_x = merkez_x + radius*np.cos(teta)            #dairenin x koordinatları
    
    x_bitis = np.copy(daire_x)          #panellerin x koordinatı ve bitiş noktaları
    y_bitis = np.empty_like(x_bitis)    #panellerin y koordinatı ve bitiş noktası
    
    x, y = np.append(x, x[0]), np.append(y, y[0]) #kapalı devre oluşturması için yapıldı.
    

    
    
    
    
    
    
    