def oblicz(brutto):
    emerytalne = brutto * (9.76 / 100)
    rentowe = brutto * (6.5 / 100)
    wypadkowe = brutto * (1.67 / 100)
    fundusz_pracy = brutto * (2.45 / 100)
    po_skladkach = brutto + emerytalne + rentowe + wypadkowe + fundusz_pracy

    return po_skladkach


kwota_brutto = int(input("Podaj kwotę brutto: "))
print(oblicz(kwota_brutto))
