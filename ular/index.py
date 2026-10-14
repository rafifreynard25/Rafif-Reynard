import pygame
import random
import sys

# 1. Inisialisasi Pygame
pygame.init()

# 2. Pengaturan Layar
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Stars!")

# 3. Warna (RGB) dengan Tema Langit Malam
SKY_BLUE = (25, 25, 112)       # Midnight Blue (Background)
BASKET_COLOR = (139, 69, 19)   # Cokelat Kayu (Keranjang)
STAR_COLOR = (255, 215, 0)     # Kuning Emas (Bintang)
TEXT_COLOR = (255, 255, 255)   # Putih untuk Teks Skor

# 4. Pengaturan Player (Keranjang Penangkap)
player_width = 110
player_height = 40
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height - 20
player_speed = 8

# 5. Pengaturan Target (Bintang yang Jatuh)
target_width = 40
target_height = 40
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = -target_height
target_speed = 5

# 6. Skor & Game Clock
score = 0
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30, bold=True)

# --- GAME LOOP UTAMA ---
running = True
while running:
    # Membatasi FPS game di angka 60
    clock.tick(60)
    
    # Kumpulkan semua input/event dari user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Pergerakan Player (Tombol Panah Kiri & Kanan)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed

    # Pergerakan Target (Bintang Jatuh dari Langit)
    target_y += target_speed

    # Jika Bintang lolos melewati bawah layar
    if target_y > SCREEN_HEIGHT:
        target_x = random.randint(0, SCREEN_WIDTH - target_width)
        target_y = -target_height

    # Deteksi Tabrakan (Sistem Kolisi)
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    
    # Menggunakan bentuk lingkaran atau kotak untuk bintang (disini kita pakai rect dengan sudut melengkung/efek visual)
    target_rect = pygame.Rect(target_x, target_y, target_width, target_height)

    if player_rect.colliderect(target_rect):
        score += 1
        target_speed += 0.2  # Game semakin lama semakin cepat
        # Reset posisi bintang ke atas
        target_x = random.randint(0, SCREEN_WIDTH - target_width)
        target_y = -target_height

    # --- GAMBAR SEMUA KE LAYAR ---
    screen.fill(SKY_BLUE)  # Background langit malam

    # Gambar Player (Keranjang dengan sedikit detail hiasan)
    pygame.draw.rect(screen, BASKET_COLOR, player_rect, border_radius=8)
    
    # Gambar Target (Bintang Berwarna Kuning Emas)
    pygame.draw.circle(screen, STAR_COLOR, (target_x + target_width // 2, target_y + target_height // 2), target_width // 2)

    # Tampilkan Skor dengan warna putih agar kontras dengan background gelap
    score_text = font.render(f"Skor: {score}", True, TEXT_COLOR)
    screen.blit(score_text, (20, 20))

    # Update Layar
    pygame.display.flip()

# Keluar dari game jika loop selesai
pygame.quit()
sys.exit()