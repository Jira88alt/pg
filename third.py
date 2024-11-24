def je_prvocislo(cislo):
    
    if cislo < 2:
        return False
    for i in range(2, int(cislo ** 0.5) + 1):  
        if cislo % i == 0:
            return False
    return True

def vrat_prvocisla(maximum):
    
    maximum = int(maximum)  # Ujistíme se, že maximum je číslo.
    return [cislo for cislo in range(2, maximum + 1) if je_prvocislo(cislo)]

if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    try:
        prvocisla = vrat_prvocisla(int(cislo))
        print(prvocisla)
    except ValueError:
        print("Prosím, zadejte platné celé číslo.")
