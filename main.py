import pygame



# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Set up the display window
window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Epic battle")

pygame.mixer.music.load('Rhythm of the Fight.mp3')
pygame.mixer.music.set_volume(0.5) 
pygame.mixer.music.play(-1)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path) 
        self.rect = self.image.get_rect()  
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, self.rect)  

hero = GameSprite("hero.png", 100, 100)
enemy = GameSprite("mage.png", 300, 300)
bg = GameSprite("bg.png", 0, 0)

sound = pygame.mixer.Sound('output.mp3')
sound.play()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic

    # Render graphics
    bg.draw()
    hero.draw()
    enemy.draw()
    pygame.display.flip()  # Update the display

# Clean up Pygame
pygame.quit()