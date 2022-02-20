from models.bullet_source import BulletSource
from models.game_object import GameObject
from models.hitbox import Hitbox


class Bullet(GameObject):
    def __init__(self, posX:int, posY:int, source:BulletSource, color):
        self.color = color
        self.height = 6
        self.width = 4
        self.movementSpeed = 0.20
        self.posX = posX-self.width/2
        self.posY = posY
        self.source = source