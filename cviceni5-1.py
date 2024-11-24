
import sys

import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for radek in reader:
        print(radek)

def nacti_csv(soubor):
    data ()
    with open(soubor, "r") as fp:
        reader = csv.reader(fp)
        for row in reader:
            data.append(row)
    return data


def spoj_data(*data):
    pass


def zapis_csv(soubor, data):
    pass


if __name__ == "__main__":
    try:
        soubor1 = sys.argv[1]
        soubor2 = sys.argv[2]
        csv_data1 = nacti_csv(soubor1)
        csv_data2 = nacti_csv(soubor2)
        print(csv_data1)
        print(csv_data2)
        vysledna_data = spoj_data(csv_data1, csv_data2)
        zapis_csv(vysledna_data)
    except Exception:
        pass
