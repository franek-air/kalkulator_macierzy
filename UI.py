import pygame
import numpy as np
import operations
import history
import file_manager

def run_gui():
    pygame.init()
    WIDTH, HEIGHT = 600, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Kalkulator Macierzowy Pro")

    # Kolory i Fonty
    WHITE, GRAY, BLUE, BLACK, GREEN, RED = (255, 255, 255), (220, 220, 220), (50, 150, 255), (0, 0, 0), (0, 150, 0), (200, 0, 0)
    font = pygame.font.SysFont("Arial", 16)
    font_small = pygame.font.SysFont("Arial", 14)

    # Stan aplikacji
    input_text_a = ""
    input_text_b = ""
    active_input_rect = None
    message = "Wprowadź macierz A i B."
    current_result = None
    history_display_text = ""
    display_mode = 'none' # 'none', 'result', 'history'

    class Button:
        def __init__(self, x, y, w, h, text, action_id):
            self.rect = pygame.Rect(x, y, w, h)
            self.text = text
            self.action_id = action_id
        def draw(self, surf):
            pygame.draw.rect(surf, BLUE, self.rect, border_radius=5)
            t = font.render(self.text, True, WHITE)
            surf.blit(t, t.get_rect(center=self.rect.center))
        def is_clicked(self, pos): return self.rect.collidepoint(pos)

    buttons = [
        Button(50, 50, 120, 35, "Dodaj A+B", "1"),
        Button(180, 50, 120, 35, "Odejmij A-B", "2"),
        Button(310, 50, 120, 35, "Pomnóż A*B", "3"),
        Button(50, 100, 120, 35, "Odwróć A", "4"),
        Button(180, 100, 120, 35, "Potęga A", "5"),
        Button(310, 100, 120, 35, "Det(A)", "6"),
        Button(440, 50, 120, 35, "Historia", "7"),
        Button(440, 100, 120, 35, "Zapisz Wynik", "save"),
        Button(50, 150, 120, 35,"Wyczyść historię","clear")
    ]

    input_rect_a = pygame.Rect(50, 580, 240, 30)
    input_rect_b = pygame.Rect(310, 580, 240, 30)

    running = True

    while running:
        screen.fill(GRAY)
        msg_surf = font.render(message, True, BLACK)
        screen.blit(msg_surf, (50, 620))

        if display_mode == 'result' and current_result is not None:
            res_str = str(current_result).split('\n')
            for i, line in enumerate(res_str[:15]): # Display first 15 lines of result
                screen.blit(font_small.render(line, True, GREEN), (50, 200 + i*18))
        elif display_mode == 'history' and history_display_text:
            hist_lines = history_display_text.split('\n')
            for i, line in enumerate(hist_lines[:15]): # Display first 15 lines of history
                screen.blit(font_small.render(line, True, BLACK), (50, 200 + i*18))

        for btn in buttons: btn.draw(screen)

        # Draw input rect A
        pygame.draw.rect(screen, WHITE, input_rect_a)
        pygame.draw.rect(screen, BLACK, input_rect_a, 2 if active_input_rect != input_rect_a else 3)
        input_surf_a = font.render(input_text_a, True, BLACK)
        screen.blit(input_surf_a, (input_rect_a.x + 5, input_rect_a.y + 7))
        screen.blit(font_small.render("Macierz A (plik lub [[..]]):", True, BLACK), (50, 560))

        # Draw input rect B
        pygame.draw.rect(screen, WHITE, input_rect_b)
        pygame.draw.rect(screen, BLACK, input_rect_b, 2 if active_input_rect != input_rect_b else 3)
        input_surf_b = font.render(input_text_b, True, BLACK)
        screen.blit(input_surf_b, (input_rect_b.x + 5, input_rect_b.y + 7))
        screen.blit(font_small.render("Macierz B (plik lub [[..]]):", True, BLACK), (310, 560))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.KEYDOWN:
                if active_input_rect == input_rect_a:
                    if event.key == pygame.K_BACKSPACE: input_text_a = input_text_a[:-1]
                    else: input_text_a += event.unicode
                elif active_input_rect == input_rect_b:
                    if event.key == pygame.K_BACKSPACE: input_text_b = input_text_b[:-1]
                    else: input_text_b += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if an input field was clicked
                if input_rect_a.collidepoint(event.pos):
                    active_input_rect = input_rect_a
                elif input_rect_b.collidepoint(event.pos):
                    active_input_rect = input_rect_b
                else:
                    active_input_rect = None # Deselect if click outside input fields

                for btn in buttons:
                    if btn.is_clicked(event.pos):
                        try:
                            if btn.action_id == "save":
                                if isinstance(current_result, np.ndarray):
                                    path = input_text_a if "." in input_text_a else "wynik.txt"
                                    file_manager.save_matrix(current_result, path)
                                    message = f"Zapisano macierz do {path}"
                                else:
                                    message = "Błąd: Można zapisywać tylko macierze, nie skalary!"
                                display_mode = 'result' # Stay in result mode after save
                                continue

                            if btn.action_id == "7": # Historia button
                                history_display_text = history.wyswietl_historie_as_string()
                                display_mode = 'history'
                                message = "Wyświetlono historię w GUI."
                                continue
                            elif btn.action_id =="clear":
                                history.wyczysc_historie()
                                history_display_text = history.wyswietl_historie_as_string()
                                display_mode = 'history'
                                message = "Wyświetlono historię w GUI."
                                continue
                            # For other operations, clear history display and set to result mode
                            history_display_text = ""
                            display_mode = 'result'

                            m1 = None
                            m2 = None

                            if btn.action_id in ["1", "2", "3"]:
                                m1_val = input_text_a.strip()
                                m2_val = input_text_b.strip()

                                if not m1_val or not m2_val:
                                    raise ValueError("Obie macierze (A i B) muszą być wprowadzone!")
                                if "." in m1_val:
                                    m1 = file_manager.load_matrix(m1_val)
                                elif "h" not in m1_val:
                                    m1 = np.array(eval(m1_val))
                                else:
                                    m1 = np.array(history.pobierz_z_historii(int(m1_val[1])))
                                #m1 = file_manager.load_matrix(m1_val) if "." in m1_val elif "h" not in m1_val np.array(eval(m1_val)) else np.array(eval(history.pobierz_z_historii(int(m1_val[2]))))
                                #m2 = file_manager.load_matrix(m2_val) if "." in m2_val else np.array(eval(m2_val))

                                if "." in m2_val:
                                    m2 = file_manager.load_matrix(m2_val)
                                elif "h" not in m2_val:
                                    m2 = np.array(eval(m2_val))
                                else:
                                    m2 = np.array(history.pobierz_z_historii(int(m2_val[1])))
                                if btn.action_id == "1": current_result = operations.dodaj_macierze(m1, m2)
                                elif btn.action_id == "2": current_result = operations.odejmij_macierze(m1, m2)
                                elif btn.action_id == "3": current_result = operations.pomnoz_macierze(m1, m2)
                            else: # Unary operations
                                m1_val = input_text_a.strip()
                                if not m1_val:
                                    raise ValueError("Macierz A musi być wprowadzona!")
                                m1 = file_manager.load_matrix(m1_val) if "." in m1_val else np.array(eval(m1_val))

                                if btn.action_id == "4": current_result = operations.odwroc_macierz(m1)
                                elif btn.action_id == "6": current_result = operations.wyznacznik_macierzy(m1)
                                elif btn.action_id == "5": current_result = operations.poteguj_macierz(m1, 2)
                                

                            history.dodaj_do_historii(btn.text, current_result)
                            message = f"Wykonano: {btn.text}"
                        except Exception as e:
                            message = f"Błąd: {str(e)}"
                            display_mode = 'none' # If error, clear display or show error message
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    run_gui()
