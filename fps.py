import pygame
import sys

class FPS:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Verdana", 20)
        self.text = self.font.render(str(self.clock.get_fps()), True, (255, 255, 255))

    def render(self, display):
        self.text = self.font.render(str(self.clock.get_fps()), True, (255, 255 ,255))
        pygame.display.set_caption('my video game. ' + 'fps: ' + str(int(self.clock.get_fps())))
        # display.blit(self.text, (200, 150))
