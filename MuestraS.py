# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 09:57:50 2022

@author: gerard
"""
from Graficame import Graf #Clase para trabajar la señal
import numpy as np #Manejo de arreglos
from scipy.io import wavfile #Para leer archivos wav

class MuestraSeñal():
    
    def __init__(self, wavname):
        self.wavname = wavname
        self.fs, data = wavfile.read(wavname)
        self.ch1 = data[:,0]
        self.ch2 = data[:,1]
        self.t = np.linspace(0,(len(self.ch1)-1)/self.fs,len(self.ch1))
    
    def GeneraWAV(self,name,fs,data):
        wavfile.write(name,int(fs), data)
    
    def Show(self, espec = False, canales = False, power = False):
        
        ch1 = self.ch1[::10]
        ch2 = self.ch1[::10]
        t = self.t[::10]
        fs = (len(t)-1)/t[-1]
        
        print("Mostrando: " + self.wavname)
        print("longitud original:{}\nfs original = {}\nlongitud resultante: {}\nfs resultante= {}".format(len(self.t),self.fs,len(t),fs))
        
        
        graficas = Graf(t,ch1,ch2,self.wavname)
        if canales:
            a = int(input("Canales que desea graficar \n1. ch1\n2. ch2\n3. Todos \n"))
            if a != 3:
                graficas.GrafVista(a)
            
            else:
                for i in range(1,a):
                    graficas.GrafVista(i)
        
        if espec:
            graficas.GrafEspectro(fs)
        
        if power:
            graficas.GrafPotencia()
        '''
        data = np.array([[ch1[n], ch2[n]] for n in range(len(ch1))])
        self.GeneraWAV("Sremuestreada.wav",fs, data.astype(np.int16));
        '''

if __name__ == "__main__":
    #Aqui va el nombre del archivo wav
    MuestraSeñal("Para_evitar_achaques_Segment_0.wav").Show(power = True)
    