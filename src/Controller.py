from Config_ha import Config_ha
from Conn_ha import Conn_ha
from Log import Log
import socket
import threading

class Controller(Config_ha):
    """
    Class for controlling program + multi-threading controll
    """

    def __init__(self):
        self.log = Log()
        self._path = "../config/config.csv"
        self.ip = None
        self.port = None
        self.time_out_sec = None
        self.list_vlaken = []
        self.program_bezi = False

    def start(self):
        self.log.load_log()
        self.program_bezi = True
        try:
            self.load_file()
        except Exception as e:
            self.log.write(e,2)
            exit(0)
        try:
            self.listen()
        except Exception as e:
            self.log.write(e, 2)
            exit(0)

    def thred_hand(self,connection,client_inet_address):
        """
        funkce volajicí třídu Conn_ha metodu control
        :param connection:
        :param client_inet_address: for iteration
        :return:
        """
        conn_ha = Conn_ha
        conn_ha.control(Conn_ha,connection)

    def listen(self):
        """
        funkce pro naslouchani na nactenem ip + portu
        po uspesnem pripojeni se pošle pomocí multi-threading do funkce 'thred_hand'
        :return: void
        """

        try:

            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)

            if self.ip == "auto":
                self.ip = IPAddr

            self.log.write("Mám ip: {} a port: {}".format(self.ip,self.port),1)

            server_inet_address = (self.ip, int(self.port))
            server_socket = socket.socket()
            server_socket.bind(server_inet_address)
            server_socket.listen()

        except Exception as e:
            self.log.write(e, 2)

        while(self.program_bezi):

            connection, client_inet_address = server_socket.accept()
            self.log.write("Client connection accepted from " + str(client_inet_address[0]) + ":" + str(client_inet_address[1]),1)

            t = threading.Thread(target=self.thred_hand, args=(connection,client_inet_address))
            t.start()
            self.list_vlaken.append(t)

        connection.close()
        for x in self.list_vlaken:
            x.kill

        self.log.write("Program se ukončil...",1)


