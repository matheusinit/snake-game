from pygame import SurfaceType
from typing import Tuple
import pygame

Position = Tuple[int, int]
Color = Tuple[int, int]

class Fruit():
    position: Position
    color: Color
    pixel: int
    surface: SurfaceType
    destroyed: bool

    def __init__(self, color, pixel, screen):
        self.color = color
        self.pixel = pixel
        self.surface = screen
        self.destroyed = False

    def draw(self, position: Position) -> None:
        x = position[0] * self.pixel
        y = position[1] * self.pixel
        object = pygame.Rect(x, y, self.pixel, self.pixel)
        pygame.draw.rect(self.surface, self.color, object)
