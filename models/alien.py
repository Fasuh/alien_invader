import pygame
from pygame.locals import *

from models.bounds import Bounds
from models.game_object import GameObject
from models.hitbox import Hitbox

class Alien(GameObject):
    def __init__(self, position:int, height:int, width:int):
        if position%3 == 0:
            self.color = (100,100,255)
        if position%3 == 1:
            self.color = (255,100,100)
        if position%3 == 2:
            self.color = (100,255,100)

        self.height = height
        self.width = width
        self.position = position
        self.posX = 0
        self.posY = 0