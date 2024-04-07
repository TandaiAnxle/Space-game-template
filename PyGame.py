import pygame
import random

pygame.init()

# Screen setup
Screen_Width = 500
Screen_Height = 500
Screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("Space Bertus")

# Player setup
Player_Width = 40
Player_Height = 60
Player_Vel = 5
player = pygame.Rect(200, Screen_Height - Player_Height, Player_Width, Player_Height)

# Projectile setup
Projectile_Width = 10
Projectile_Height = 10
Projectile_Vel = 5
projectiles = []

# Background setup
BG = pygame.transform.scale(pygame.image.load("Galxy.jpg"), (Screen_Width, Screen_Height))

# Font setup
font = pygame.font.SysFont(None, 36)

# Clock setup
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

# Function to create a new projectile
def create_projectile():
    x = random.randint(0, Screen_Width - Projectile_Width)
    y = 0
    return pygame.Rect(x, y, Projectile_Width, Projectile_Height)

# Function to draw text on the screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    Screen.blit(text_surface, (x, y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    Screen.blit(BG, (0, 0))

    # Draw the player rectangle
    pygame.draw.rect(Screen, "red", player)

    # Move and draw projectiles
    for projectile in projectiles:
        pygame.draw.rect(Screen, "Green", projectile)
        projectile.y += Projectile_Vel
        if projectile.colliderect(player):
            # Display "Game Over" message and restart option
            Screen.fill((0, 0, 0))  # Clear the screen
            draw_text("Game Over", font, (255, 255, 255), Screen_Width//2 - 80, Screen_Height//2 - 18)
            draw_text("Press R to restart", font, (255, 255, 255), Screen_Width//2 - 120, Screen_Height//2 + 18)
            pygame.display.update()
            # Wait for player to press 'R' to restart
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        player = pygame.Rect(200, Screen_Height - Player_Height, Player_Width, Player_Height)
                        projectiles.clear()
                        start_time = pygame.time.get_ticks()  # Reset start time
                        break
                else:
                    continue
                break
        if projectile.y > Screen_Height:
            projectiles.remove(projectile)

    # Create new projectiles randomly
    if random.randint(1, 100) == 1:
        projectiles.append(create_projectile())

    # Update the display
    pygame.display.update()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player.x - Player_Vel >= 0:
        player.x -= Player_Vel
    if keys[pygame.K_d] and player.x + Player_Vel + player.width <= Screen_Width:
        player.x += Player_Vel

    # Calculate and display elapsed time
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    draw_text("Time: " + str(elapsed_time), font, (255, 255, 255), 10, 10)

    clock.tick(60)

pygame.quit()
