class Slovicka:

    def hledej(self,slovicko):
        """
        funkce pro hledání překladu

        :param slovicko: str
        :return: False když nenajde, Přeložené slovíčko pokud najde
        """

        slovicka_dic = ("cat", "kocka"), ("dog", "pes"), ("giraffe", "žirafa"), ("lion", "lev"), ("bird", "pták")

        for x in slovicka_dic:
            if x[0] == slovicko:
                return x[1]
        return False
