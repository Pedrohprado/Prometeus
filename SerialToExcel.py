#Import librays
import serial
import xlwt
from datetime import datetime
import keyboard
import threading



class serialToExcel:

    def __init__(self,port, speed):

        self.port = port
        self.speed = speed
        self.wb = xlwt.Workbook()
        self.ws = self.wb.add_sheet("Prometeus", cell_overwrite_ok=True)
        self.ws.write(0,0, "Prometeus")
        self.ws.write(1,1,"Amperagem")
        self.ws.write(1,2, "Situação")
        self.columns = ["Time"]
        self.number = 100
        self.i = 0

    def setColumns(self,col):
        self.columns.extend(col)

    def setRecordsNumber(self, number):
        self.number = number

    def readPort(self):
        ser = serial.Serial(self.port, self.speed, timeout=1)
        c = 0

        def verificaKeyPress(): #Criando function para finalizar o código atráves da letra 'q';
            while True:
                if keyboard.is_pressed('q'):
                    self.i = self.number

        for col in self.columns:
            self.ws.write(1,c,col)
            c = c + 1
            self.fila = 2


            while(self.i<self.number):
                line = ser.readline().decode('utf-8') #Colocando na var line = a corrente que está passando na serial

                if (len(line) > 1): #O valor de entrada for maior que 1 então ele
                    now = datetime.now()
                    date_time = now.strftime("%H:%M:%S")
                    situation = "trabalhando"
                    print(date_time, line, situation)
                    if(line.find(",")):
                        c = 1
                        self.ws.write(self.fila, 0, date_time)
                        columns = line.split(',')

                        for col in columns:
                            self.ws.write(self.fila, c, col)
                            self.ws.write(self.fila, 2, situation)

                            c = c + 1
                    self.i = self.i + 1
                    self.fila = self.fila + 1

                else:
                    now = datetime.now()
                    date_time = now.strftime("%H:%M:%S")
                    situation2 = "parado"
                    print(date_time, 0, situation2)
                    if (line.find(",")):
                        c = 1
                        self.ws.write(self.fila, 0, date_time)
                        columns = line.split(',')

                        for col in columns:
                            self.ws.write(self.fila, c, col)
                            self.ws.write(self.fila, c, 0)
                            self.ws.write(self.fila,2,situation2)

                            c = c + 1

                    self.i = self.i + 1
                    self.fila = self.fila + 1

                    threading.Thread(target=verificaKeyPress).start()

    def writeFile(self,archivo): #Salvando o arquivo em excel
        self.wb.save(archivo)