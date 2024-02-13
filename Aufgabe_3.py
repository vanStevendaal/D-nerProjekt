# KA 1 - Aufgabe 3 -  Solarpanel-Leistung
# Autor: Stefan Rosemann
# Klassenarbeit 1 2023-10
# Erstellungsdatum: 01.10.2023

print("-------------------------")
print("Solarpanel-Leistung")
print("-------------------------")

# Eingabe
version = input("Geben Sie bitte die Version des Solarpanels ein (A/S): ")
nl = int(input("Geben Sie bitte die Nennleistung des Solarpanels in Watt ein: "))
zeit = int(input("Geben Sie bitte die Betriebszeit in Jahren ein: "))



if version == "A":
    leistung =(nl*0.975)
    for i in range(1,zeit):
        leistung *= 0.994

if version == "S":
    leistung =(nl*0.98)
    for i in range (1,zeit):
        leistung *= 0.9945
    

#Ausgabe
print(f"\nNach {zeit} Betriebsjahren beträgt die Leistung des Solarpanels {round(leistung,1)} Watt.")
