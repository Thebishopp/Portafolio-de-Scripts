import glob
import os
import sys
import time
import pandas as pd
import datetime
import _thread
import telebot
###telebot###
token =  #TOKEN de TeleBot#
tb = telebot.TeleBot(token)
#tb.send_message("-1001555555919", "test")
### GENERADOR DE LISTA ###
listxt = open("patentes.txt", "r") #Archivo .txt con las patentes buscandas
domread = listxt.read()
pat_buscadas = domread.split(",")
listxt.close()
print(type(pat_buscadas))
print(pat_buscadas)
### GENERADOR DE LISTA ###
def detect(tkndir, TXT, tknname): ### función detect###
    x = 0
    while x < 1:
        now = datetime.datetime.now()
        hora = now.strftime("%H:%M:%S")
        date = now.strftime("%d/%m/%Y, %H:%M:%S")
        csv = glob.glob(tkndir, recursive=True)
        ultcsv = max(csv, key=os.path.getmtime)
        df = pd.read_csv(ultcsv, sep = ";")
        dominio = df.iloc[-1, 1]
        dominio2 = df.iloc[-1, 4]
        #print(dominio)
        if dominio in pat_buscadas:
            print(hora + " " + dominio + " | " + dominio2)
            asd = open(TXT, "a")
            asd.write("\n" + date + ";" + dominio + ";" + dominio2)
            asd.close()
            tb.send_message("-1001555555919", "{} Dominio: {} ha sido detectado por {}".format(hora, dominio, tknname))
            print(hora + ":" + dominio + " " + "ha sido detectado por:" + " " + tknname)
            time.sleep(120) #Delay de dos minutos tras una patente detectada, evita la reiteración de notificaciones
            continue
        else:
            time.sleep(3) #Delay de tres segundos para no sobrecargar CPU
            continue
### función###
_thread.start_new_thread (detect,('?:/???/???/**/*.csv', "exata.txt", "Totem Piedras"))
_thread.start_new_thread (detect,('?:/???/???/**/*.csv', "sakura.txt", "Totem Sakura"))
_thread.start_new_thread (detect,('?:/???/???/**/*.csv', "193.txt", "Totem 193"))
_thread.start_new_thread (detect,('?:/???/???/**/*.csv', "192.txt", "Totem 192"))
_thread.start_new_thread (detect,('?:/???/???/**/*.csv', "exata_2.txt", "Exata 2"))
