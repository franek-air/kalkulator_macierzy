# history.py - Moduł zarządzania historią operacji (Osoba E)

# Globalna lista przechowująca zadania. 
# Każde zadanie to słownik: {'opis': str, 'wynik': np.array}
_historia = []

def dodaj_do_historii(opis_dzialania, macierz_wynikowa):
    """
    Dodaje nowy wpis do historii. Pilnuje limitu 10 zadań.
    Jeśli historia przekroczy 10, usuwa najstarszy element.
    """
    if len(_historia) >= 10:
        _historia.pop(0)  # Usuwa pierwszy (najstarszy) element
    
    nowy_wpis = {
        'opis': opis_dzialania,
        'wynik': macierz_wynikowa
    }
    _historia.append(nowy_wpis)
    print(f"✅ Dodano do historii: {opis_dzialania}")

def wyswietl_historie():
    """Wypisuje sformatowaną listę ostatnich 10 zadań."""
    if not _historia:
        print("\n📭 Historia jest pusta.")
        return

    print("\n--- OSTATNIE 10 ZADAŃ ---")
    for i, wpis in enumerate(_historia):
        print(f"[{i}] Operacja: {wpis['opis']}")
        # Wyświetlamy macierz (używamy str(), bo numpy ładnie formatuje macierze)
        print(f"    Wynik:\n{wpis['wynik']}\n")

def pobierz_z_historii(indeks):
    """Zwraca macierz wynikową z konkretnego zadania na podstawie indeksu."""
    try:
        indeks = int(indeks)
        return _historia[indeks]['wynik']
    except (IndexError, ValueError, TypeError):
        print("❌ Błąd: Nieprawidłowy numer zadania w historii.")
        return None

def wyczysc_historie():
    """Całkowicie czyści pamięć zadań."""
    _historia.clear()
    print("🗑️ Historia została wyczyszczona.")
