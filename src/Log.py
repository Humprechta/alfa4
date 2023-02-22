from os.path import exists
from datetime import datetime

class Log():
    """
    Třída pro manipulování s logem v csv
    """

    def file_append(self,content : str):
        """
        Funkce pro připsání do souboru, pokud soubor neexistuje, založí se

        :param content str
        """
        if not exists(self._static_path):
            with open(self._static_path,"x","utf-8") as file:
                pass
        with open(self._static_path,"a") as file:
            file.write(content)

    def write(self,co_se_stalo,priorita):
        """
        Funkce na seřazení dat do csv formátu (str)

        :param co_se_stalo str - co se má logovat
        :param priorita int co se stalo 1 info, 2 = err ...
        """
        now = datetime.now() # current date and time
        csv_parse = "{} - ;{};{}#\n".format(co_se_stalo,priorita,now.strftime("%m/%d/%Y, %H:%M:%S"))

        if not exists("../log/log.csv"):
            with open("../log/log.csv", "x", "utf-8") as file:
                pass
        with open("../log/log.csv", "a") as file:
            file.write(csv_parse)

    def load_log(self):
        """
        Načtení dat z log_file

        :return str ze souboru
        """
        with open("../log/log.csv","r") as file:
            return file.read()

    def data_parse(self):
        """
        Parse data (#\n)

        :retrun list
        """
        data = self.load_log()
        return data.split("#\n")

    def data_parse_in(self,array):
        """
        Funkce na parsování jednotlivých řédek/záznamů (;)

        :return list[list]
        """
        list_parse = []
        for x in array:
            y = x.split(";")
            list_parse.append(y)
        return list_parse

    def data_to_string(self,input):
        """
        Formátování dat ze souboru do čitelné formy

        :param input list[list]
        :return str
        """
        str = ""
        i = 0;
        for x in input:
            i = i + 1
            str = "{} {}. {} datum: {}\n".format(str,i,x[0],x[2])
        return str

    def return_data(self,input : int, descending : int):
        """
        Funkce pro řazení/filtrování dat

        :param input int - nastavení od uživatele 1-3
        :param descending int jesli uživatel chce data od nejnovějších či od nejstarších
        :retrun list
        """

        list = []
        data = self.data_parse()
        data = self.data_parse_in(data)
        data.pop()

        if input == 1:
            for x in data:
                if x[1] == "2":
                    list.append(x)
        elif input == 2:
            for x in data:
                if x[1] != "2":
                    list.append(x)
        elif input == 3:
            for x in data:
                list.append(x)
        elif input !=1 or input != 3 or input !=2:
            raise Exception("Špatně zadaná hodnota")

        if descending == 2:
            list.reverse()

        return self.data_to_string(list)



