import pygame
from pygame.locals import *

from models.tick import Tick

class TimeController:
    def __init__(self):
        pass

    def tick(self) -> Tick:
        return Tick(delta = pygame.time.Clock().tick(60))