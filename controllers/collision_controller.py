from typing import List
import pygame

from pygame.locals import *
from controllers.alien_controller import AlienController

from controllers.bullets_controller import BulletsController
from controllers.player_controller import PlayerController
from models.bullet_source import BulletSource
from models.game_result import GameResult


class CollisionController:
    def __init__(self, playerController:PlayerController, bulletsController:BulletsController, aliensController:AlienController):
        self.playerController = playerController
        self.bulletsController = bulletsController
        self.aliensController = aliensController

    def checkCollisions(self) -> GameResult:
        bullets = self.bulletsController.bullets

        player = self.playerController.player
        playerHitbox = player.getHitbox()

        aliens = self.aliensController.aliens

        for bullet in bullets:
            if bullet.source == BulletSource.PLAYER:
                for alien in aliens:
                    alienHitbox = alien.getHitbox()
                    if alienHitbox.collidesWithOther(bullet.getHitbox()):
                        result = self.aliensController.notyfyHit(alien)
                        self.bulletsController.notifyHit(bullet)
                        if result == GameResult.WIN:
                            return result
            elif bullet.source == BulletSource.ALIEN:
                if playerHitbox.collidesWithOther(bullet.getHitbox()):
                    self.bulletsController.notifyHit(bullet)
                    self.playerController.notyfyHit()
                    return GameResult.LOSS
