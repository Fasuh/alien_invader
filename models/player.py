import pygame
from pygame.locals import *

from models.bounds import Bounds
from models.game_object import GameObject
from models.hitbox import Hitbox
from models.movement import Movement
from models.tick import Tick


class Player(GameObject):
    def __init__(self, bounds: Bounds):
        self.color = (255, 255, 255)
        self.height = 20
        self.width = 20
        self.posX = bounds.width/2
        self.posY = bounds.height - self.height - 5
        self.movementSpeed = 0.33

    def die(self):
        self.color = (255, 0, 0)
