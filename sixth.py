import sys
import requests
import re


def download_url_and_get_all_hrefs(url):
    """
    Funkce stáhne obsah zadané URL pomocí requests.get(), zkontroluje,
    zda je navrátový kód 200, a najde všechny odkazy ve formátu <a href="url">.
    Tyto odkazy vrátí jako seznam.
    """
    hrefs = []

    try:
        # Stáhnutí obsahu stránky
        response = requests.get(url)
        
        # Kontrola status kódu
        if response.status_code == 200:
            # Extrakce obsahu stránky
            page_content = response.text
            
            # Použití regulárního výrazu pro nalezení všech odkazů
            hrefs = re.findall(r'<a\s+href="([^"]+)"', page_content)
        else:
            print(f"Chyba: Status kód {response.status_code} při stahování URL: {url}")
    except Exception as e:
        print(f"Chyba při stahování nebo zpracování URL: {e}")

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        # Zavolání funkce a výpis výsledků
        links = download_url_and_get_all_hrefs(url)
        print("Nalezené odkazy:")
        for link in links:
            print(link)
    except Exception as e:
        print(f"Program skončil chybou: {e}")
