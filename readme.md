############################### Vítáme vás v manuálu alfa4 1.0 - Vášista ################################

@Author: Václav Taitl C4b, jako školní projekt pro SPŠE Ječná (Praha 2, Ječná 30) @Date: 2023-02-21

# Ke spuštění potřebujete operační systém win10+ čí unix s aplikací python (verze 3.9+), spuští se přes /src/main.py

# Aplikace může běžet jako démon, všechny výpisy jsou v souboru /log/log.csv

# Program funguje jako P2P aplikace, kdy poslouchá na 3 základní commandy (viz níže)

# Program překládá slova z AJ od ČJ

# program umí sám tyto slovíčka: cat, dog, girrafe, bird, lion

# Commands:
1. TRANSLATEPING"jmeno programu" => program odpovídá zpět ve tvaru TRANSLATEPONG"Vášista" + spojení zůstává
2. TRANSLATELOCL"slovo k prekladu" => program odpovídá zpět buď přeloženým slovem ve tvaru TRANSLATEDSUC"přeložené slovo" + ukončí spojení, nebo TRANSLATEDERR"Neumím..." + ukončí spojení
3. TRANSLATESCAN"slovo k prekladu" => program odpovídá zpět buď přeloženým slovem ve tvaru TRANSLATEDSUC"přeložené slovo" + ukončí spojení, nebo TRANSLATEDERR"Neumím..." + ukončí spojení

# Config soubor (/config/config.csv) auto = ip from PC
posloucham_ip:<auto/IPv4>;
posloucham_prort:<cislo portu>;
time_out_sec:<sekundy>;

# Pokud máte nějaké dotazy, neváhejte mě kontaktovat vasek.taitl@gmail.com# Program je volně k použití ZDARMA, je pod licencí Creative Commons - BY