def bin_to_dec(binarni_cislo):
    # Pokud je binární číslo typu int, převedeme ho na řetězec
    if isinstance(binarni_cislo, int):
        binarni_cislo = str(binarni_cislo)
    
    # Převedeme binární řetězec na desítkové číslo
    return int(binarni_cislo, 2)

def test_funkce():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128
    assert bin_to_dec("10011101") == 157  # Test pro 10011101 -> 157
    assert bin_to_dec(10011101) == 157  # Test pro 10011101 jako číslo

# Spuštění testů
test_funkce()
