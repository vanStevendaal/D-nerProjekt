# KA 1 - Aufgabe 1 -  PV-Amortisationsrechnung
# Autor: Stefan Rosemann
# Klassenarbeit 1 2023-10
# Erstellungsdatum: 01.10.2023

print("-------------------------")
print("PV-Amortisationsrechnung")
print("-------------------------")

insta_kosten = 1500
verguetung = 0.082
jahresertrag = 1000


# Eingabe
kwp = int(input("Geben Sie bitte die zu installierende Leistung in kWp ein: "))
preis = int(input("Geben Sie bitte ihren aktuellen Strompreis in ct/kWh ein: "))
verbrauch = int(input("Geben Sie bitte ihren aktuellen Eigenverbrauch in kWh ein: "))

#Verarbeitung

leistung = (jahresertrag*kwp)
bau_kosten = (kwp*insta_kosten)
eigenver_ersp = (verbrauch*(preis/100))
einspeisung_ersp = ((leistung-verbrauch)*verguetung)
einnahmen = (eigenver_ersp+ einspeisung_ersp)

zeit= (bau_kosten/einnahmen)


#Ausgabe
print("\nDie Amortisationszeit beträgt ",round(zeit,2),"Jahre.")