# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 09:57:50 2022

@author: Ortiz Montufar Gerardo
"""
from Graficame import Graf #Clase para trabajar la señal
import numpy as np #Manejo de arreglos
from scipy.io import wavfile #Para leer archivos wav

class MuestraSeñal():
    """
        Esta clase muestra una señal, recibe el nombre de un archivo wav para leerlo
        MuestraSeñal('nombre.wav')
        
        Parameters
        ----------
        wavname : string
                  Nombre del archivo wav "ejemplo.wav"
    """
    
    def __init__(self, wavname):
        
        self.wavname = wavname
        self.fs, data = wavfile.read(wavname)
        self.ch1 = data[:,0]
        self.ch2 = data[:,1]
        self.t = np.linspace(0,(len(self.ch1)-1)/self.fs,len(self.ch1))
    
    def GeneraWAV(self,name,fs,data):
        """
        MuestraSeñal.Generawav(name, fs, data) Gebera un archivo wav, este se genera en la carpeta donde se ejecuta el programa
        
        Parameters
        ----------
        name : string
               Nombre del nuevo archivo wav
               
        fs   : int
               Frecuencia de muestreo
               
        data : array
               Contenido que deberá llevar el nuevo archivo wav
        
        """
        wavfile.write(name,int(fs), data)
    
    def Show(self, espec = False, canales = False, power = False):
        """
            MuestraSeñal.Show(espec, canales, power) muestra las graficas del espectro de la señal, los canales o la potencia de la señal
            si los parámetros se ingresan como True
            
            Parameters
            ----------
            espec   : boolean, opcional
                      Se inicializa como True si se quiere calcular y graficar el espectro de la señal mediante la transformada de fourier con el método FFT
                      
            canales : boolean, opcional
                      Se inicializa como True si se requiere graficar los canales. Dado este caso se realiza un casting en consola preguntando qué canal se requiere
                      se selecciona
                      1 Si se requiere el canal 1
                      2 Si se requiere el canal 2
                      3 Ambos se grafican
             
            power   : boolean, opcional
                      Se inicializa con true si se requiere calcular y graficar la potencia de la señal. Aunque, no en la forma convencional. La parte negativa se refleja
                      con el fin de tener un mejor apreciacion de la morfología original en especial de las variaciones tonales (vibraciones por segundo)
        """
        
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
        

if __name__ == "__main__":
    """
        Aqui va el nombre del archivo wav
        Si se requiere ver los canales si el archivo es estereo, dentro de Show colocar canales = True
        Para ver el espectro espec = True
        Para mostrar todo la sintaxis sería: Show(power = True, canales = True, espec = True)
    """
    MuestraSeñal("Para_evitar_achaques_Segment_0.wav").Show(power = True)
    
