def oblicz(brutto):
    emerytalne = brutto * (9.76 / 100)
    rentowe = brutto * (1.5 / 100)
    chorobowe = brutto * (2.45 / 100)
    zdrowotne = brutto * (7.77 / 100)
    po_skladkach = brutto - emerytalne - rentowe - chorobowe - zdrowotne
    zaliczka_PIT = po_skladkach * (17 / 100)
    netto = po_skladkach - zaliczka_PIT
    return netto


brutto = int(input("Podaj zarobki brutto: "))
netto = oblicz(brutto)
print("kwota netto:", round(netto, 2))
