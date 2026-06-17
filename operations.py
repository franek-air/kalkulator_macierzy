import numpy as np

# OSOBA B:
def dodaj_macierze(A, B):
    """
    Dodaje dwie macierze element-po-elemencie.
    Przyjmuje listy lub numpy.array. Zwraca numpy.array lub string z błędem.
    """
    try:
        A_np = np.asarray(A)
        B_np = np.asarray(B)
        return np.add(A_np, B_np)
    except Exception as e:
        return f"Błąd podczas dodawania: {e}"

def odejmij_macierze(A, B):
    """
    Odejmuje macierz B od macierzy A (element-po-elemencie).
    Przyjmuje listy lub numpy.array. Zwraca numpy.array lub string z błędem.
    """
    try:
        A_np = np.asarray(A)
        B_np = np.asarray(B)
        return np.subtract(A_np, B_np)
    except Exception as e:
        return f"Błąd podczas odejmowania: {e}"

def pomnoz_macierze(A, B):
    """
    Mnoży macierze (iloczyn macierzowy).
    Przyjmuje listy lub numpy.array. Zwraca numpy.array lub string z błędem.
    """
    try:
        A_np = np.asarray(A)
        B_np = np.asarray(B)
        # Używamy mnożenia macierzowego (matmul)
        return np.matmul(A_np, B_np)
    except ValueError as e:
        return f"Błąd kształtu podczas mnożenia macierzy: {e}"
    except Exception as e:
        return f"Błąd podczas mnożenia: {e}"

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
    