import numpy as np
import os

def load_matrix(path:str):
    if not os.path.exists(path):
        # print(f"❌ Nie odnaleziono pliku: {path}")
        return None

    # Wykrywanie separatora na podstawie rozszerzenia
    if path.endswith(".csv"):
        separator = ","
    elif path.endswith(".txt"):
        separator = None # NumPy domyślnie radzi sobie z białymi znakami w txt
    else:
        separator = None

    try:
        matrix = np.genfromtxt(path, delimiter=separator)

        if matrix.size == 0 or np.isnan(matrix).all():
            raise ValueError("Plik jest pusty lub ma zły format!")

        if matrix.ndim == 1:
            matrix = matrix.reshape(1, -1)

        return matrix

    except Exception as e:
        # print(f"❌ Błąd podczas wczytywania: {e}")
        return None

def save_matrix(matrix, path:str):
    """
    Zapisuje macierz do pliku .txt (tab-separated) lub .csv (comma-separated).
    """
    try:
        if path.endswith(".csv"):
            np.savetxt(path, matrix, delimiter=",", fmt='%g')
        else:
            # Domyślnie zapisujemy jako txt
            if not path.endswith(".txt"):
                path += ".txt"
            np.savetxt(path, matrix, delimiter="\t", fmt='%g')
        # print(f"✅ Macierz zapisana do pliku: {path}")
        return True
    except Exception as e:
        # print(f"❌ Błąd podczas zapisu: {e}")
        return False
