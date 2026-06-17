import numpy as np

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
    print(f"Dodano do historii: {opis_dzialania}")

def wyswietl_historie_as_string():
    if not _historia:
        return "Historia jest pusta."
    
    wpisy_z_indeksami = list(enumerate(_historia))[-9:]
    col_width = 24
    output_lines = ["--- HISTORIA ---", ""]
    
    for i in range(0, len(wpisy_z_indeksami), 3):
        chunk = wpisy_z_indeksami[i:i+3]
        columns_text_lines = []
        
        for orig_idx, wpis in chunk:
            col_lines = []
            col_lines.append(f"[{orig_idx}] {wpis['opis']}")
            
            matrix_lines = str(wpis['wynik']).split('\n')
            matrix_lines = ["         " + line for line in matrix_lines]
            
            col_lines.extend(matrix_lines)
            columns_text_lines.append(col_lines)
        
        max_lines = max(len(lines) for lines in columns_text_lines)
        
        for line_idx in range(max_lines):
            row_parts = []
            for col_lines in columns_text_lines:
                text = col_lines[line_idx] if line_idx < len(col_lines) else ""
                row_parts.append(text.ljust(col_width))
            
            output_lines.append(" | ".join(row_parts))
        
        total_row_length = col_width * len(chunk) + 3 * (len(chunk) - 1)
        output_lines.append("-" * total_row_length)
        output_lines.append("")
        
    return "\n".join(output_lines)

def pobierz_z_historii(indeks):
    """Zwraca macierz wynikową z konkretnego zadania na podstawie indeksu."""
    try:
        indeks = int(indeks)
        return _historia[indeks]['wynik']
    except (IndexError, ValueError, TypeError):
        print("Błąd: Nieprawidłowy numer zadania w historii.")
        return None

def wyczysc_historie():
    """Całkowicie czyści pamięć zadań."""
    _historia.clear()
    print("Historia została wyczyszczona.")
