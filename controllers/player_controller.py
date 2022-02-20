import pygame

from typing import List
from pygame.locals import *

from pygame.event import Event
from controllers.bullets_controller import BulletsController
from decorators.debounce import Debounce
from models.bounds import Bounds
from models.movement import Movement
from models.player import Player
from models.tick import Tick


class PlayerController:
    def __init__(self, player: Player, bounds: Bounds, bulletController: BulletsController):
        self.player = player
        self.movementBuffor: List[Movement] = list()
        self.bounds = bounds
        self.bulletController = bulletController
        self.shootsBullets: bool = False

    def bufforKeys(self, events: List[Event]):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.movementBuffor.append(Movement.LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.movementBuffor.append(Movement.RIGHT)
                elif event.key == pygame.K_SPACE:
                    self.shootsBullets = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.movementBuffor.remove(Movement.LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.movementBuffor.remove(Movement.RIGHT)
                elif event.key == pygame.K_SPACE:
                    self.shootsBullets = False

    def move(self, tick: Tick):
        if self.movementBuffor:
            movement = self.movementBuffor[-1]
            distance = self.player.movementSpeed * tick.delta * movement.value
            maxDistance = self.bounds.width - 5 - self.player.width
            self.player.posX = min(
                max(5, self.player.posX + distance), maxDistance)

        if self.shootsBullets:
            self.shootBullet()

    @Debounce(0.5)
    def shootBullet(self):
        self.bulletController.registerPlayerBullet(player=self.player)

    def notyfyHit(self):
        self.player.die()