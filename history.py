import numpy as np

historia_operacji = []

def dodaj_do_historii(operacja: str, wynik):
    historia_operacji.append((operacja, wynik))

def wyswietl_historie_as_string():
    if not historia_operacji:
        return "Brak historii.\n\n"

    history_str = "--- Historia Operacji ---\n"
    for i, (op, res) in enumerate(historia_operacji):
        history_str += f"{i+1}. Operacja: {op}\n"
        # Limit display for matrices to prevent huge output
        if isinstance(res, np.ndarray):
            res_lines = str(res).split('\n')
            for line_idx, line in enumerate(res_lines):
                if line_idx >= 5: # Limit to 5 lines of matrix display
                    history_str += "   ... (więcej)\n"
                    break
                history_str += f"   {line}\n"
        else:
            history_str += f"   Wynik: {res}\n"
    history_str += "-------------------------"
    return history_str

def wyczysc_historie():
    global historia_operacji
    historia_operacji = []
