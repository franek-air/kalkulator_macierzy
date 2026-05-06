import numpy as np

# OSOBA B:
def dodaj_macierze(A, B):
    # podpowiedź: return np.add(A, B)
    pass

def odejmij_macierze(A, B):
    pass

def pomnoz_macierze(A, B):
    pass

# OSOBA C
def odwroc_macierz(A):
    try:
        return np.linalg.inv(A)
    except np.linalg.LinAlgError:
        return "Błąd: Macierz jest osobliwa, nie można jej odwrócić."

def poteguj_macierz(A, n):
    try:
        return np.linalg.matrix_power(A, n)
    except Exception as e:
        return f"Błąd podczas potęgowania: {e}"

# funkcja dodatkowa
def wyznacznik_macierzy(A):
    try:
        wynik = np.linalg.det(A)
        return round(wynik, 4)
    except Exception as e:
        return f"Błąd podczas obliczania wyznacznika: {e}"
    