def cislo_text(cislo):
    prvni = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    druhy = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    treti = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    
    zadaneCislo = int(cislo)
    
    if zadaneCislo < 10:
        return prvni[zadaneCislo]
    elif 10 <= zadaneCislo < 20:
        return druhy[zadaneCislo - 10]
    elif 20 <= zadaneCislo < 100:
        druhy_cast = treti[zadaneCislo // 10]
        prvni_cast = prvni[zadaneCislo % 10] if zadaneCislo % 10 != 0 else ""
        return f"{druhy_cast} {prvni_cast}".strip()
    elif zadaneCislo == 100:
        return "sto"
    else:
        return "Číslo je vyšší než 100"

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
