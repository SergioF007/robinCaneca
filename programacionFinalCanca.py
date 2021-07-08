#sudo apt-get install python3-serial  ó pip install serial
import serial
#import Arduino~
import pandas as pd
#sudo apt-get install csv python3  ó  sudo pip3 install python-csv
import csv
#sudo apt-get  install python3-numpy
import numpy as np
from time import sleep, strftime, time
from datetime import time as tm
from datetime import datetime, date, timedelta
#	sudo apt install python3-picamera
from picamera import PiCamera
from time import sleep
arduino = serial.Serial('/dev/ttyACM0',9600)  
arduino.setDTR(False)
sleep(1)
arduino.flushInput()
arduino.setDTR(True)
c = []
i = []
u = []
p = []
t = []
nombre = []
material = []
def  leer_arduino():
   lineBytes = arduino.readline()
   line = lineBytes.decode('utf-8').strip()
   print(line)
   
try:
  while True:
     leer_arduino()
     # Separamos los datos recibidos mediante el seprador "|"
     #capacitivo, inductivo, ultrasonico, peso, sFin = line.split("|", 4) 
     s1,s2,s3,s4,sFin = line.split("|", 4)    
     capacitivo = s1
     inductivo = s2
     ultrasonico =s3
     peso = s4 
     c.append(int(capacitivo))
     i.append(int(inductivo)) 
     u.append(int(ultrasonico))
     p.append (float(peso))
     t.append(strftime("%H:%M:%S")) # %Y-%m-%d 
     print("nombre")
     nombre.append(str(input()))
     print("material")
     material.append(str(input()))
     tiempo=np.array(t)
     sensor1=np.array(c)
     sensor2=np.array(i)
     sensor3=np.array(u)
     sensor4=np.array(p)
     nombreObjeto=np.array(nombre)
     tipoMaterial=np.array(material)
     data={'tiempo': tiempo,'Capacitivo': sensor1, 'inductivo': sensor2, 'ultrasonico': sensor3, 'peso': sensor4, 'nombreObjeto': nombre, 'tipoMaterial': material }
     df=pd.DataFrame(data)
     print(df)
     # nombreArchivo = strftime("%Y-%M-%D")
     nombreArchivo = str(datetime.now().year)+"-"+str(+datetime.now().month)+"-"+str(datetime.now().day)
     df.to_csv(nombreArchivo+"MatrizSensores.csv")
     df.to_excel(nombreArchivo+"Matriz.xlsx")
except keyboardInterrupt:
   arduino.close()
   exit()