from typing import List
from models.alien import Alien
from models.bounds import Bounds
from models.bullet import Bullet
from models.bullet_source import BulletSource
from models.player import Player
from models.tick import Tick

class BulletsController:
    def __init__(self, bounds:Bounds):
        self.bullets: List[Bullet] = list()
        self.bounds = bounds

    def registerEnemyBullet(self, alien:Alien):
        posX = alien.posX+(alien.width/2)
        posY = alien.posY
        self.bullets.append(Bullet(posX=posX, posY=posY, source=BulletSource.ALIEN, color=alien.color))

    def registerPlayerBullet(self, player:Player):
        posX = player.posX+(player.width/2)
        posY = player.posY
        self.bullets.append(Bullet(posX=posX, posY=posY, source=BulletSource.PLAYER, color=(255, 255, 255)))

    def bulletsTick(self, tick:Tick):
        for bullet in self.bullets:
            if bullet.source == BulletSource.PLAYER:
                distance = bullet.movementSpeed*tick.delta
                bullet.posY -= distance
                if bullet.posY+bullet.height <= -5:
                    self.bullets.remove(bullet)
            elif bullet.source == BulletSource.ALIEN:
                distance = bullet.movementSpeed*tick.delta
                bullet.posY += distance
                if bullet.posY+bullet.height >= self.bounds.height+5:
                    self.bullets.remove(bullet)

    def notifyHit(self, bullet:Bullet):
        self.bullets.remove(bullet)
