# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:20:26 2022

@author: Ortiz Montufar Gerardo
"""

import matplotlib.pyplot as plt #Para graficar
import scipy.fft as spf #Grafica el espectro de una señal
import numpy as np #manejo de arreglos

class Graf():
    def __init__(self,t,x1,x2,nombre):
        
        self.t = t
        self.x1 = x1
        self.x2 = x2
        self.nombre = nombre
        
    def Muestra(self, x, etiqueta):
        
        plt.figure(figsize=(15, 5))
        plt.plot(self.t, x, color = 'r', label = etiqueta)
        plt.title(self.nombre)
        plt.xlabel('segundos')
        plt.ylabel('Amplitud')
        plt.grid(linestyle=':')
        plt.legend();
    
    def GrafEspectro(self,fs):
        
        N = len(self.x1)
        X = spf.fft(self.x1)
        f = np.linspace(0,N-1,N)*fs/N
        plt.figure(figsize=(15, 5))
        plt.plot(f, 20*np.log10(abs(X)), ls=':', lw=1, marker='.', mfc='r')
        #plt.axvline(freq, ls=':',color='r')
        plt.axvline(fs/2, ls='--',color='purple',label='$fs/2$')
        plt.xlabel('f (Hz)')
        plt.ylabel('Magnitud (dB)')
        plt.title(self.nombre)
        plt.grid(linestyle=':')
        plt.legend();
        
    
    def GrafVista(self, canal):
        
        if canal == 1:
            etiqueta = "CH1"
            x = self.x1/1000
        else:
            etiqueta = "CH2"
            x = self.x2/1000
        
        self.Muestra(x,etiqueta + " $x10^3$")
        
    def GrafSumaCh(self):
        self.Muestra((self.x1 + self.x2)/1000, "Suma ch1 + ch2 $x10^3$")
        
    def GrafPotencia(self):
        xc = self.x1 + self.x2
        
        x = xc*(xc >= 0)/1000
        x = np.power(x,2)
        y = xc*(xc <= 0)/1000
        y = (-1)*np.power(y,2)
        xc = x+y
        
        '''
        y = (xc*(xc <= 0))**2
        y = y*(-1)
        xc = x + y
        '''
        
        self.Muestra(xc, "Potencia en $Megas x10^6$ (parte negativa añadida y reflejada)")
        
