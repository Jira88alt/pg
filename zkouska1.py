# Příklad 1: Práce s podmínkami a řetězci
# Zadání:
# Napište funkci `find_divisible`, která přijme číslo max_number a dělitel divisor. 
# Funkce vrátí seznam všech čísel menších nebo rovno max_number, která jsou dělitelná beze zbytku dělitelem divisor.
# Příklad: find_divisible(5, 2) vrátí [2, 4].

# Definice funkce
def find_divisible(max_number, divisor):
    # ZDE NAPIŠTE VÁŠ KÓD
    # Seznam, který uloží dělitelná čísla
    divisible_numbers = []
    
    # Program projde všechna čísla od 1 do 100 (začne u 1 a přidává +1 dokud se nedostane k podmínce max_number)
    for number in range(1, max_number + 1):
        # Pokud je číslo dělitelné bez zbytku, přidáme ho do seznamu (čísla jako 1.5 se do seznamu nemohou dostat)
        if number % divisor == 0:
            # Metoda append je funkce, která přidává prvek na konec seznamu
            divisible_numbers.append(number)
    
    # Vracíme seznam dělitelných čísel
    return divisible_numbers
    pass


# Unit testy
# Definice funkce
def test_find_divisible():
    assert find_divisible(25, 5) == [5, 10, 15, 20, 25]
    assert find_divisible(9, 3) == [3, 6, 9]
    assert find_divisible(13, 2) == [2, 4, 6, 8, 10, 12]

# Podmínka
if __name__ == "__main__":
    max_number = 100
    divisor = int(input("Enter divisor: "))
    result = find_divisible(max_number, divisor)
    print(f'Čísla dělitelné {divisor} které jsou menší nebo rovny {max_number}: {result}')