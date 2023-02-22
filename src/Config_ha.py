from Log import Log

class Config_ha:
    """
    class for loading config log
    """
    def _read_file(self):

        with open(self._path, "r") as file:
            return file.read()

    def load_file(self):
        """
        Load file, if file not found or isn´t readable raise Exeption
        Return list in list, first index is znacky, second is boty
        :return: list
        """

        try:
            data = self._read_file()
        except:
            raise Exception("Soubor se nepovedlo otevřít")
        self._parse_data(data)

    def _parse_data(self,data):
        log = Log
        data = self._parse_to_row(data)
        self._parse_all(data)

    def _parse_all(self,list):
        temp_list = []
        if len(list) != 3:
            raise "Špatně nakonfigurovaný config.csv soubor, podívejte se do dokumentace"
        for x in list:

            data = x.split(":")
            temp_list.append(data)

        self.ip = temp_list[0][1]
        self.port = temp_list[1][1]
        self.time_out_sec = temp_list[2][1].replace(";","")

    def _parse_to_row(self,data):
        return data.split(";\n")
