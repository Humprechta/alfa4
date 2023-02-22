from Log import Log
import time
from Slovicka import Slovicka
import socket

class Conn_ha():
    """
    Class for commands handling...
    """

    def TRANSLATEPING(self):
        return "TRANSLATEPONG\"Vášista\""
    def TRANSLATELOCL(self,slovo):
        return "TRANSLATELOCL\"{}\"".format(slovo)
    def TRANSLATEDSUC(self,slovo):
        return "TRANSLATEDSUC\"{}\"".format(slovo)
    def TRANSLATEDERR(self):
        return "TRANSLATEDERR\"{}\"".format("Neumím...")
    def TRANSLATESCAN(self,slovo):
        return self.TRANSLATEDSUC(slovo)

    def command_ha(self,data):
        """
        comand handling
        :param data: str commands from network
        :return:
        """
        data = data.strip().replace("\n\r","")

        log = Log()
        log.write("přišlo po síti: " + data, 1)

        data = data.split("\"")

        if data[0] == "TRANSLATEPING":
            return (1,self.TRANSLATEPING(self))
        elif data[0] == "TRANSLATELOCL" or data[0] == "TRANSLATESCAN":
            slovicka = Slovicka
            slovicka = slovicka.hledej(self,data[1])
            if slovicka == False:
                return (0, self.TRANSLATEDERR(self))
            return (0,self.TRANSLATEDSUC(self,slovicka))
        else:
            return (0,self.TRANSLATEDERR(self))

    def control(self,conn):
        """
        :param conn: connection
        :return: void
        """

        pripojeno = True
        while(pripojeno):
            data = None

            valid_daat = True
            while(valid_daat):
                data = conn.recv(1024).decode("utf-8")
                data.strip()
                if len(data) > 2:
                    valid_daat = False

            data = self.command_ha(self,data)
            log = Log()
            log.write("odpoved: "+data[1],1)

            message_as_bytes = bytes(data[1], "utf-8")
            conn.send(message_as_bytes)
            if data[0] == 0:
                pripojeno = False

        time.sleep(0.4)
        conn.close()







