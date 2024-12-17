def dev_to_bin(cislo):
    # Funkce konvertuje decimální číslo na binární reprezentaci
    # Vstup: cislo (str nebo int)
    # Výstup: binární řetězec (str)
    if isinstance(cislo, str):
        cislo = int(cislo)  # Převod na int, pokud je vstup řetězec
    return bin(cislo)[2:]  # Použití funkce bin() a odstranění prefixu "0b"

# Testování funkce
def test_dev_to_bin():
    assert dev_to_bin(167) == "10011101"
    assert dev_to_bin("167") == "10011101"
    assert dev_to_bin(0) == "0"
    assert dev_to_bin("1") == "1"
    assert dev_to_bin(255) == "11111111"
    assert dev_to_bin("128") == "10000000"
