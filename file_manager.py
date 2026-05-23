import numpy as np
import os
def load_matrix(path:str):
    if not os.path.exists(path):
        raise FileNotFoundError("Nie odnaleziono pliku o takiej nazwie :( ")


    if path.endswith(".csv"):
        separator = ","
    else: separator = None
    try:
        matrix = np.genfromtxt(path, delimiter=separator)

        if matrix.size == 0 or np.isnan(matrix).all() or np.isnan(matrix).any():
            raise ValueError("Plik jest pusty, albo ma zły format, albo oba!! :(")

        if matrix.ndim == 1:
            matrix = matrix.reshape(1, -1)

        return matrix

    except PermissionError:
        print("Brak uprawnień do pliku :(")

    except ValueError as e:
        print("Błąd danych : {e} :(")
        return None