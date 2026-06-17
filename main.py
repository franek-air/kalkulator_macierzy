import operations
import history
import file_manager
import numpy as np

def get_matrix_input(label):
    print(f"\n--- Wybór macierzy {label} ---")
    print("1. Wczytaj z pliku")
    print("2. Pobierz z historii")
    print("3. Wprowadź ręcznie (np. [[1,2],[3,4]])")
    choice = input("Wybór: ")
    
    if choice == '1':
        path = input("Podaj nazwę pliku (np. macierz.csv): ")
        return file_manager.load_matrix(path)
    elif choice == '2':
        history.wyswietl_historie()
        idx = input("Podaj numer indeksu z historii: ")
        return history.pobierz_z_historii(idx)
    elif choice == '3':
        try:
            val = input("Wpisz macierz jako listę list: ")
            return np.array(eval(val))
        except:
            print("Błędny format!")
            return None
    return None

def execute_matrix_logic(op_type, matrix_a, matrix_b=None, power=1):
    result = None
    desc = ""
    if op_type == "1":
        result = operations.dodaj_macierze(matrix_a, matrix_b)
        desc = "Dodawanie"
    elif op_type == "2":
        result = operations.odejmij_macierze(matrix_a, matrix_b)
        desc = "Odejmowanie"
    elif op_type == "3":
        result = operations.pomnoz_macierze(matrix_a, matrix_b)
        desc = "Mnożenie"
    elif op_type == "4":
        result = operations.odwroc_macierz(matrix_a)
        desc = "Odwracanie"
    elif op_type == "5":
        p = int(input("Podaj potęgę: "))
        result = operations.poteguj_macierz(matrix_a, p)
        desc = f"Potęgowanie ({p})"
    elif op_type == "6":
        result = operations.wyznacznik_macierzy(matrix_a)
        desc = "Wyznacznik"

    if isinstance(result, (np.ndarray, float, int, np.number)):
        history.dodaj_do_historii(desc, result)
        print("\nWynik:\n", result)
        
        # Opcja zapisu do pliku po wyświetleniu
        save_choice = input("\nCzy chcesz zapisać wynik do pliku? (t/n): ").lower()
        if save_choice == 't':
            file_path = input("Podaj nazwę pliku (np. wynik.txt lub wynik.csv): ")
            file_manager.save_matrix(result, file_path)
    else:
        print("\nBłąd:", result)

def main():
    while True:
        print("\n=== KALKULATOR MACIERZOWY ===")
        print("1. Dodawanie\n2. Odejmowanie\n3. Mnożenie\n4. Odwracanie\n5. Potęgowanie\n6. Wyznacznik\n7. Pokaż historię\n8. Wyczyść historię\n0. Wyjście")
        op = input("Wybierz operację: ")
        
        if op == '0': break
        if op in ['7']: history.wyswietl_historie(); continue
        if op in ['8']: history.wyczysc_historie(); continue
        
        if op in ['1', '2', '3', '4', '5', '6']:
            m1 = get_matrix_input("A")
            if m1 is None: continue
            
            m2 = None
            if op in ['1', '2', '3']:
                m2 = get_matrix_input("B")
                if m2 is None: continue
            
            execute_matrix_logic(op, m1, m2)

if __name__ == '__main__':
    main()
