import pygame
import sys

# 1. Inisialisasi Pygame
pygame.init()

# 2. Pengaturan Layar
SCREEN_WIDTH = 360
SCREEN_HEIGHT = 520
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Kalkulator Python")

# 3. Warna (Tema Modern / Dark Mode)
BG_COLOR = (30, 30, 30)
SCREEN_BG = (20, 20, 20)
TEXT_WHITE = (255, 255, 255)
BTN_GRAY = (60, 60, 60)
BTN_HOVER = (80, 80, 80)
BTN_ORANGE = (255, 140, 0)
BTN_ORANGE_HOVER = (255, 165, 0)
BTN_DARK = (45, 45, 45)

# 4. Font
font_screen = pygame.font.SysFont("Arial", 40, bold=True)
font_btn = pygame.font.SysFont("Arial", 26, bold=True)

# 5. State Kalkulator
current_input = "0"
expression = ""

# Layout Tombol (Label, x, y, width, height, color, hover_color)
buttons = [
    # Baris 1
    ("C", 20, 140, 70, 60, BTN_DARK, BTN_HOVER),
    ("(", 100, 140, 70, 60, BTN_DARK, BTN_HOVER),
    (")", 180, 140, 70, 60, BTN_DARK, BTN_HOVER),
    ("/", 260, 140, 80, 60, BTN_ORANGE, BTN_ORANGE_HOVER),
    
    # Baris 2
    ("7", 20, 210, 70, 60, BTN_GRAY, BTN_HOVER),
    ("8", 100, 210, 70, 60, BTN_GRAY, BTN_HOVER),
    ("9", 180, 210, 70, 60, BTN_GRAY, BTN_HOVER),
    ("*", 260, 210, 80, 60, BTN_ORANGE, BTN_ORANGE_HOVER),
    
    # Baris 3
    ("4", 20, 280, 70, 60, BTN_GRAY, BTN_HOVER),
    ("5", 100, 280, 70, 60, BTN_GRAY, BTN_HOVER),
    ("6", 180, 280, 70, 60, BTN_GRAY, BTN_HOVER),
    ("-", 260, 280, 80, 60, BTN_ORANGE, BTN_ORANGE_HOVER),
    
    # Baris 4
    ("1", 20, 350, 70, 60, BTN_GRAY, BTN_HOVER),
    ("2", 100, 350, 70, 60, BTN_GRAY, BTN_HOVER),
    ("3", 180, 350, 70, 60, BTN_GRAY, BTN_HOVER),
    ("+", 260, 350, 80, 60, BTN_ORANGE, BTN_ORANGE_HOVER),
    
    # Baris 5
    ("0", 20, 420, 150, 60, BTN_GRAY, BTN_HOVER),
    (".", 180, 420, 70, 60, BTN_GRAY, BTN_HOVER),
    ("=", 260, 420, 80, 60, BTN_ORANGE, BTN_ORANGE_HOVER),
]

# --- GAME LOOP UTAMA ---
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Klik kiri mouse
                for label, bx, by, bw, bh, color, hover in buttons:
                    if bx <= mouse_pos[0] <= bx + bw and by <= mouse_pos[1] <= by + bh:
                        if label == "C":
                            current_input = "0"
                            expression = ""
                        elif label == "=":
                            try:
                                # Menghitung hasil ekspresi matematika menggunakan eval() aman untuk lokal
                                result = str(eval(expression + current_input))
                                current_input = result
                                expression = ""
                            except Exception:
                                current_input = "Error"
                                expression = ""
                        elif label in ["+", "-", "*", "/"]:
                            if current_input != "Error":
                                expression += current_input + " " + label + " "
                                current_input = "0"
                        else: # Tombol Angka atau Titik (.)
                            if current_input == "0" or current_input == "Error":
                                current_input = label
                            else:
                                current_input += label

    # --- GAMBAR KE LAYAR ---
    screen.fill(BG_COLOR)

    # Kotak Layar Kalkulator
    screen_rect = pygame.Rect(20, 20, 320, 100)
    pygame.draw.rect(screen, SCREEN_BG, screen_rect, border_radius=10)
    pygame.draw.rect(screen, (70, 70, 70), screen_rect, width=2, border_radius=10)

    # Render teks riwayat ekspresi di atas
    expr_surface = font_btn.render(expression, True, (150, 150, 150))
    screen.blit(expr_surface, (35, 30))

    # Render teks input/hasil kalkulator di bawah
    text_surface = font_screen.render(current_input, True, TEXT_WHITE)
    # Membuat teks rata kanan di layar kalkulator
    text_rect = text_surface.get_rect(right=325, bottom=110)
    screen.blit(text_surface, text_rect)

    # Gambar Tombol-tombol Kalkulator
    for label, bx, by, bw, bh, color, hover in buttons:
        btn_rect = pygame.Rect(bx, by, bw, bh)
        
        # Efek Hover saat kursor di atas tombol
        if bx <= mouse_pos[0] <= bx + bw and by <= mouse_pos[1] <= by + bh:
            pygame.draw.rect(screen, hover, btn_rect, border_radius=8)
        else:
            pygame.draw.rect(screen, color, btn_rect, border_radius=8)
            
        # Tulis label di tengah tombol
        label_surface = font_btn.render(label, True, TEXT_WHITE)
        label_rect = label_surface.get_rect(center=btn_rect.center)
        screen.blit(label_surface, label_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()