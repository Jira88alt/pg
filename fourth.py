def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    def na_sachovnici(pozice):
        return 1 <= pozice[0] <= 8 and 1 <= pozice[1] <= 8

    def je_cesta_volna(start, cil, smer):
        r, c = start
        dr, dc = smer
        while (r, c) != cil:
            r += dr
            c += dc
            if (r, c) in obsazene_pozice:
                return False
        return True

    typ = figurka["typ"]
    start = figurka["pozice"]
    r1, c1 = start
    r2, c2 = cilova_pozice

    if not na_sachovnici(cilova_pozice):
        return False
    if cilova_pozice in obsazene_pozice:
        return False

    if typ == "pěšec":
        if c1 == c2 and (r2 == r1 + 1 or (r1 == 2 and r2 == 4 and (r1 + 1, c1) not in obsazene_pozice)):
            return True
        if abs(c2 - c1) == 1 and r2 == r1 + 1 and cilova_pozice in obsazene_pozice:
            return True

    elif typ == "jezdec":
        return (abs(r2 - r1), abs(c2 - c1)) in [(2, 1), (1, 2)]

    elif typ == "věž":
        if r1 == r2 or c1 == c2:
            smer = (0, 1) if r1 == r2 else (1, 0) if c1 == c2 else (0, 0)
            if je_cesta_volna(start, cilova_pozice, smer):
                return True

    elif typ == "střelec":
        if abs(r2 - r1) == abs(c2 - c1):
            smer = (1 if r2 > r1 else -1, 1 if c2 > c1 else -1)
            if je_cesta_volna(start, cilova_pozice, smer):
                return True

    elif typ == "dáma":
        if r1 == r2 or c1 == c2 or abs(r2 - r1) == abs(c2 - c1):
            smer = (0, 1) if r1 == r2 else (1, 0) if c1 == c2 else (1 if r2 > r1 else -1, 1 if c2 > c1 else -1)
            if je_cesta_volna(start, cilova_pozice, smer):
                return True

    elif typ == "král":
        return max(abs(r2 - r1), abs(c2 - c1)) == 1

    return False
