import pygame
from pygame.locals import *

from controllers.alien_controller import AlienController
from controllers.bullets_controller import BulletsController
from controllers.collision_controller import CollisionController
from controllers.player_controller import PlayerController
from models.bounds import Bounds
from models.game_result import GameResult
from models.player import Player
from models.tick import Tick


class GameController:
    def __init__(self, bounds: Bounds):
        self.bounds = bounds
        self.player = Player(bounds=bounds)
        self.bulletsController = BulletsController(bounds=self.bounds)
        self.playerController = PlayerController(
            player=self.player, bounds=bounds, bulletController=self.bulletsController)
        self.aliensController = AlienController(bulletController=self.bulletsController, bounds=self.bounds)
        self.aliensController.generateAliens(numberOfRows=3, bounds=bounds)
        self.aliens = self.aliensController.aliens
        self.collisionController = CollisionController(
            playerController=self.playerController, aliensController=self.aliensController, bulletsController=self.bulletsController)
        self.hasStarted = False
        self.result:GameResult = None
        self.startRound()

    def startRound(self):
        self.hasStarted = True

    def roundTick(self, tick: Tick):
        if self.hasStarted:
            self.bulletsController.bulletsTick(tick=tick)
            self.aliensController.shoot()
            self.aliensController.alienTick(tick=tick)
            result = self.collisionController.checkCollisions()
            if result is not None:
                self.finishWithResult(result)

    def playerTick(self, events, tick: Tick):
        if self.hasStarted:
            if(events):
                self.playerController.bufforKeys(events)

        self.playerController.move(tick=tick)

    def finishWithResult(self, result:GameResult):
        self.hasStarted = False
        self.result = result
