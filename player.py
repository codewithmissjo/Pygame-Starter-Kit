import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/p1_jump.png')
        self.rect = self.image.get_rect()
        self.speed = pygame.math.Vector2(1, 0)
    
    def update(self):
        self.rect.move_ip(self.speed)




# setting up player speed with a vector!
# -- define speed: self.speed = pygame.math.Vector2(1, 0)
# -- apply speed: self.rect.move_ip(self.speed)
# -- call in main game loop

# infinite x axis movement

# player key based movement
# player facing