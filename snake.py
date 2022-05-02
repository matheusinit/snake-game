from pygame import SurfaceType
from typing import Tuple, List
import pygame

# Types
Position = Tuple[int, int]
Body = List[Position]
Color = Tuple[int, int]


class Snake():
    body: Body
    color: Color
    pixel: int
    surface: SurfaceType
    last_removed: Position
    

    """
    | Instantiate object
    """
    def __init__(self, color, pixel, screen):
        self.color = color
        self.pixel = pixel
        self.surface = screen
        self.body = [(0, 0)]


    """
    | Draw snake pixel at time, at each position of X and Y
    """
    def draw(self) -> None:
        for i, pos in enumerate(self.body):
            object = pygame.Rect(pos[0] * self.pixel, pos[1] * self.pixel, self.pixel, self.pixel)
            pygame.draw.rect(self.surface, self.color, object)
    
    """
    | Remove tail (last element) and inserts new element at head (first element)
    """
    def move(self, position: Position) -> None:
        self.last_removed = self.body[-1]
        self.body.pop()
        self.body.insert(0, position)

        # Insert update_head method in here
    
    """
    | Increases the body of the snake
    """
    def increase_body(self, position: Position = None) -> None:
        if position == None:
            position = self.last_removed
        self.body.append(position)
    
    """
    | Update the head of the snake, in case of going out of border
    """
    def update_head(self, position: Position) -> None:
        del self.body[0]
        self.body.insert(0, position)




