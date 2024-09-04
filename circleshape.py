import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.contrainers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.position = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes musst override
        pass

    def update(self, dt):
        # sub-classes musst override
        pass

    
